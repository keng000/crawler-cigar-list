from typing import Dict

import pandas as pd


def format(df: pd.DataFrame) -> Dict[str, str]:
    """
    Create a announcement text from data frame elements.
    It returns a list of formatted text whenever the record has only one or not.
    """

    block = """
## {section}
{content}
"""
    announcements = {}
    df.fillna("???", inplace=True)

    for _, row in df.iterrows():
        body = ""
        for idx, val in row.iteritems():
            body += block.format(section=idx, content=val)

        announcements[f"{row['brand']} {row['name']}"] = body

    return announcements
