from typing import Tuple

import pandas as pd
from tabulate import tabulate

from .interface import FormatterInterface


class MarkdownFormatter(FormatterInterface):
    def format(self, series: pd.Series) -> Tuple[str, str]:
        table = tabulate(series.to_frame(), headers=("", ""), tablefmt="pipe")
        title = f'{series["brand"]} {series["name"]}'
        return title, table
