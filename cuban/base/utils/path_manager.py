from pathlib import Path


class PathManager:
    ROOT = Path(__file__).resolve().parents[2]
    TMP = ROOT / "tmp"
