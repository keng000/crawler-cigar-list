from environs import Env

env = Env()
env.read_env()

HATENA_USER_NAME = env.str("HATENA_USER_NAME", None)
HATENA_API_KEY = env.str("HATENA_API_KEY", None)
HATENA_BLOG_NAME = env.str("HATENA_BLOG_NAME", None)

# s3://{bucket-name}/{prefix}
S3_FURI = env.str("S3_FURI")

# gcs://{bucket-name}/{prefix}
GCS_FURI = env.str("GCS_FURI", None)
