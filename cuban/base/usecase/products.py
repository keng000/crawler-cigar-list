from logging import getLogger

import pandas as pd

logger = getLogger(__name__)


def has_diff(base: pd.DataFrame, concerned: pd.DataFrame) -> pd.DataFrame:
    """
    Compare pandas DataFrame and check the difference `right` from `left`
    Args:
        base: the base dataframe referred to.
        concerned: concerned dataframe that has a difference or not.

    Returns:

    """

    df = pd.concat([base, concerned])
    df.reset_index(drop=True)
    df_gpby = df.groupby(list(df.columns))
    idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]
    return concerned.loc[idx].reset_index(drop=True)
