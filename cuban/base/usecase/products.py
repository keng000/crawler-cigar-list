import pandas as pd


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
        query = (
            f"brand == '{b}' & name == '{n}' & shape == '{s}' & release == '{r}' & factory == '{f}' & date == '{d}'"
        )
        exists = len(base.query(query))
        assert exists < 2, ValueError(f"Suspected duplicate keys: QUERY=> {query}")
        return exists == 1

    return concerned.apply(isin_df, axis=1)
