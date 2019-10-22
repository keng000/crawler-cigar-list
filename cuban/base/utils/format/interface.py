from abc import ABC, abstractmethod
from typing import Tuple

import pandas as pd


class FormatterInterface(ABC):
    @abstractmethod
    def format(self, series: pd.Series) -> Tuple[str, str]:
        """
        Returns:
            Tuple[str, str]: title and content
        """
        pass


class FormatterController:
    def __init__(self, impl: FormatterInterface):
        if not isinstance(impl, FormatterInterface):
            raise RuntimeError("Interface Error")

        self.impl = impl

    def format(self, series: pd.Series):
        return self.impl.format(series)
