import pandas as pd

from logging import getLogger

logger = getLogger(__name__)


def has_diff(base: pd.DataFrame, concerned: pd.DataFrame) -> pd.Series:
    """
    Compare pandas DataFrame and check the difference `right` from `left`
    Args:
        base: the base dataframe referred to.
        concerned: concerned dataframe that has a difference or not.

    Returns:

    """

    def isin_df(x: pd.Series):
        b, n, s, r, f, d = x["brand"], x["name"], x["shape"], x["release"], x["factory"], x["date"]
        query = f"brand == @b & name == @n & shape == @s & release == @r & factory == @f & date == @d"

        result = base.query(query)
        exists = len(result)
        if exists > 1:
            logger.debug(result.to_string())
            raise ValueError(f"Suspected duplicate records: Key => {result.index.tolist()}, QUERY=> {query}")
        return exists == 1

    return concerned.apply(isin_df, axis=1)
