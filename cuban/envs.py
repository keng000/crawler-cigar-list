from environs import Env
from pathlib import Path
env = Env()
env.read_env(Path(__file__).parent / ".env")
