import base64
import datetime
import hashlib
import random
from logging import getLogger

import requests

from cuban.envs import HATENA_USER_NAME, HATENA_API_KEY, HATENA_BLOG_NAME

logger = getLogger(__name__)


def wsse(username: str, api_key: str) -> str:
    created = datetime.datetime.now().isoformat() + "Z"
    b_nonce = hashlib.sha1(str(random.random()).encode()).digest()
    b_digest = hashlib.sha1(b_nonce + created.encode() + api_key.encode()).digest()
    c = 'UsernameToken Username="{0}", PasswordDigest="{1}", Nonce="{2}", Created="{3}"'
    return c.format(username, base64.b64encode(b_digest).decode(), base64.b64encode(b_nonce).decode(), created)


def post_hatena(title, body):
    assert HATENA_BLOG_NAME, ValueError("Check the EnvVar")
    assert HATENA_API_KEY, ValueError("Check the EnvVar")
    assert HATENA_USER_NAME, ValueError("Check the EnvVar")

    template = """<?xml version="1.0" encoding="utf-8"?>
        <entry xmlns="http://www.w3.org/2005/Atom"
               xmlns:app="http://www.w3.org/2007/app">
          <title>{0}</title>
          <author><name>name</name></author>
          <content type="text/plain">{1}</content>
          <updated>2013-09-05T00:00:00</updated>
          <app:control>
            <app:draft>yes</app:draft>
          </app:control>
        </entry>
        """
    data = template.format(title, body).encode()

    headers = {
        "X-WSSE": wsse(HATENA_USER_NAME, HATENA_API_KEY),
        "Accept": "application/x.atom+xml, application/xml, text/xml, */*",
    }
    url = f"https://blog.hatena.ne.jp/{HATENA_USER_NAME}/{HATENA_BLOG_NAME}/atom/entry"
    r = requests.post(url, data=data, headers=headers)
    if r.status_code == 200 or r.status_code == 201:
        logger.info("Blog post success")
    else:
        logger.error(f"Blog post failed. status code: {r.status_code}")
        logger.debug(f"message: {r.text}\n\ndata:{data}")
