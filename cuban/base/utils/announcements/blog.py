import base64
import datetime
import hashlib
import random
from logging import getLogger
from xml.sax.saxutils import escape

import requests

from cuban.envs import HATENA_API_KEY, HATENA_BLOG_NAME, HATENA_USER_NAME

from .interface import AnnouncementControllerInterface

logger = getLogger(__name__)

template = """<?xml version="1.0" encoding="utf-8"?>
<entry xmlns="http://www.w3.org/2005/Atom"
       xmlns:app="http://www.w3.org/2007/app">
  <title>{title}</title>
  <author><name>keng000</name></author>
  <content type="text/x-markdown">{body}</content>
  <updated>{updated}T01:00:00+09:00</updated>
  <app:control>
    <app:draft>{draft}</app:draft>
  </app:control>
</entry>
"""


class HatenaController(AnnouncementControllerInterface):
    """
    References:
    http://developer.hatena.ne.jp/ja/documents/blog/apis/atom
    """

    def post(self, title: str, body: str):
        assert HATENA_BLOG_NAME, ValueError("Check the EnvVar")
        assert HATENA_API_KEY, ValueError("Check the EnvVar")
        assert HATENA_USER_NAME, ValueError("Check the EnvVar")
        date = datetime.datetime.today().strftime("%Y-%m-%d")
        data = self._create_blog_content(title=title, body=body, updated=date, is_draft=False)
        self._post_request(data)

    def _wsse(self, username: str, api_key: str) -> str:
        created = datetime.datetime.now().isoformat() + "Z"
        b_nonce = hashlib.sha1(str(random.random()).encode()).digest()
        b_digest = hashlib.sha1(b_nonce + created.encode() + api_key.encode()).digest()
        c = 'UsernameToken Username="{0}", PasswordDigest="{1}", Nonce="{2}", Created="{3}"'
        return c.format(username, base64.b64encode(b_digest).decode(), base64.b64encode(b_nonce).decode(), created)

    def _create_blog_content(self, title: str, body: str, updated: str, is_draft: bool = False) -> bytes:
        """
        Recent Content type: text/x-markdown
        When to make it draft, rewrite it to `<app:draft>yes</app:draft>`
        TODO: <category term={category} />
        """
        return template.format(title=title, body=escape(body), updated=updated, draft=["no", "yes"][is_draft]).encode()

    def _post_request(self, data: bytes):
        headers = {
            "X-WSSE": self._wsse(HATENA_USER_NAME, HATENA_API_KEY),
            "Accept": "application/x.atom+xml, application/xml, text/xml, */*",
        }
        url = f"https://blog.hatena.ne.jp/{HATENA_USER_NAME}/{HATENA_BLOG_NAME}/atom/entry"
        r = requests.post(url, data=data, headers=headers)
        if r.status_code == 201:
            logger.info("Blog post success")
            logger.debug(data.decode("utf8"))
            return r
        else:
            logger.error(f"Blog post failed. status code: {r.status_code}")
            logger.debug(f"message: {r.text}")
            logger.debug(f"data:{data.decode('utf8')}")
            r.raise_for_status()
