from datetime import datetime as d, timedelta as delta
from pathlib import Path

import luigi
import pandas as pd
from luigi.contrib import s3, gcs
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from cuban.base.usecase import products
from cuban.base.utils.announcements import AnnouncementController, HatenaController
from cuban.base.utils.format import FormatterController, MarkdownFormatter
from cuban.base.utils.path_manager import PathManager
from cuban.cuban.spiders.products import ProductsSpider
from cuban.envs import S3_FURI, GCS_FURI


class Crawl(luigi.Task):
    file_path = luigi.Parameter(default=PathManager.TMP / f"{d.now().strftime('%Y%m%d')}.csv")

    def output(self):
        return luigi.LocalTarget(str(self.file_path))

    def run(self):
        settings = get_project_settings()
        settings.set("FEED_URI", f"file://{self.output().path}")
        suffix = Path(self.output().path).suffix.replace(".", "")
        settings.set("FEED_FORMAT", suffix)
        proc = CrawlerProcess(settings)

        proc.crawl(ProductsSpider)
        proc.start()


class S3Upload(luigi.Task):
    """
    Requirement EnvVar: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
    References: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html
    """

    def output(self):
        file_path = f"{d.now().strftime('%Y%m%d')}.csv"
        return s3.S3Target(f"{S3_FURI}/{file_path}")

    def run(self):
        client = s3.S3Client()
        client.put(Crawl().output().path, self.output().path)

    def requires(self):
        return Crawl()


class GCSUpload(luigi.Task):
    """
    Requirement EnvVar: GOOGLE_APPLICATION_CREDENTIALS
    References:https://cloud.google.com/docs/authentication/production#auth-cloud-implicit-python
    """

    def output(self):
        file_path = f"{d.now().strftime('%Y%m%d')}.csv"
        return gcs.GCSTarget(f"{GCS_FURI}/{file_path}")

    def run(self):
        client = gcs.GCSClient()
        client.put(Crawl().output().path, self.output().path)

    def requires(self):
        return Crawl()


class Diff(luigi.Task):
    # default: previous date collection
    prev_file_name = luigi.Parameter(default=f"{(d.now() - delta(days=1)).strftime('%Y%m%d')}.csv")

    def output(self):
        return luigi.LocalTarget("/tmp/hello")

    def run(self):
        recent_file = S3Upload().output()
        # dependency
        prev_file = s3.S3Target(f"{S3_FURI}/{self.prev_file_name}")
        if not prev_file.exists():
            raise RuntimeError("File not exists in storage:", self.prev_file_name)

        with prev_file.open("r") as fp:
            prev_df = pd.read_csv(fp)

        with recent_file.open("r") as fp:
            recent_df = pd.read_csv(fp)

        # The difference is the new record
        new_arrivals = products.has_diff(prev_df, recent_df)
        logger.info(f"Diff cnt: {len(new_arrivals)}")
        logger.debug(new_arrivals.to_string())

        controller = AnnouncementController(HatenaController())
        formatter = FormatterController(MarkdownFormatter())
        for _, item in new_arrivals.iterrows():
            title, body = formatter.format(item)
            controller.post(title, body)

    def requires(self):
        return [S3Upload()]


if __name__ == "__main__":
    from logging import getLogger, DEBUG, INFO, Formatter, StreamHandler

    fmt = Formatter("[%(levelname)s]\t%(asctime)s.%(msecs)dZ\t%(message)s")
    logger = getLogger()
    logger.setLevel(DEBUG)
    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    luigi.run()
