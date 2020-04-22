from pathlib import Path

import pandas as pd
import pandas.testing

from cuban.base.usecase.products import has_diff
from cuban.base.utils.path_manager import PathManager


def test_has_diff():
    prev_file = PathManager.TEST_ROOT / "data" / "20200325.csv"
    recent_file = PathManager.TEST_ROOT / "data" / "20200326.csv"
    ans_file = PathManager.TEST_ROOT / "data" / "usecase_products_has_diff_ans.csv"

    with prev_file.open("r") as fp:
        prev_df = pd.read_csv(fp, index_col=False)

    with recent_file.open("r") as fp:
        recent_df = pd.read_csv(fp, index_col=False)

    with ans_file.open("r") as fp:
        ans_df = pd.read_csv(fp, index_col=False)

    ret = has_diff(prev_df, recent_df)
    pandas.testing.assert_frame_equal(ret, ans_df)
