from environs import Env
from pathlib import Path

env = Env()
env.read_env(Path(__file__).parent / ".env")

HATENA_USER_NAME = env.str("HATENA_USER_NAME", None)
HATENA_API_KEY = env.str("HATENA_API_KEY", None)
HATENA_BLOG_NAME = env.str("HATENA_BLOG_NAME", None)
