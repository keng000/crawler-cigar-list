from datetime import datetime as d, timedelta as delta
from pathlib import Path
import pandas as pd

import luigi
from luigi.contrib import s3
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from cuban.cuban.spiders.products import ProductsSpider
from cuban.base.utils.path_manager import PathManager
from cuban.base.usecase import products


class Crawl(luigi.Task):
    file_path = luigi.Parameter(default=PathManager.TMP / f"{d.now().strftime('%Y%m%d')}.csv")

    def output(self):
        return luigi.LocalTarget(self.file_path)

    def run(self):
        settings = get_project_settings()
        settings.set("FEED_URI", f"file://{self.output().path}")
        suffix = Path(self.output().path).suffix.replace(".", "")
        settings.set("FEED_FORMAT", suffix)
        proc = CrawlerProcess(settings)

        proc.crawl(ProductsSpider)
        proc.start()


class Upload(luigi.Task):
    def output(self):
        file_path = f"{d.now().strftime('%Y%m%d')}.csv"
        return s3.S3Target(f"s3://keng000-cigardb/daily/{file_path}")

    def run(self):
        client = s3.S3Client()
        client.put(Crawl().output().path, self.output().path)

    def requires(self):
        return Crawl()


class Diff(luigi.Task):
    # デフォルトは前日分のリストと比較
    prev_file_path = luigi.Parameter(default=PathManager.TMP / f"{(d.now() - delta(days=1)).strftime('%Y%m%d')}.csv")

    def output(self):
        pass

    def run(self):
        recent_file = Crawl().output()
        prev_file = s3.S3Target(f"s3://keng000-cigardb/daily/{self.prev_file_path}")
        if not prev_file.exists():
            raise RuntimeError("File not exists in s3:", self.prev_file_path)

        with prev_file.open("w") as fp:
            prev_df = pd.read_csv(fp)

        with recent_file.open("w") as fp:
            recent_df = pd.read_csv(fp)

        # The difference is the new record
        is_new = ~products.has_diff(prev_df, recent_df)
        new_arrival = recent_df[is_new]

    def requires(self):
        return [Crawl(), Upload()]


if __name__ == "__main__":
    luigi.run()
