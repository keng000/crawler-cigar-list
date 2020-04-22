import pandas as pd

from cuban.base.utils.format.markdown import MarkdownFormatter
from cuban.base.utils.path_manager import PathManager


def test_format():
    df = pd.read_csv(PathManager.TEST_ROOT / "data" / "20200325.csv", index_col=False)
    series = df.loc[0]
    m = MarkdownFormatter()
    title, table = m.format(series)

    with (PathManager.TEST_ROOT / "data" / "utils_markdown_format_ans.txt").open("r") as f:
        ans = f.read()

    assert table == ans
