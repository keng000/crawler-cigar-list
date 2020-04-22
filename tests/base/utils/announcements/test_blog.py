import sys

from cuban.base.utils.announcements.blog import HatenaController


def test_post():
    c = HatenaController()

    title = "test_title"
    body = "test_body"
    date = "2010-01-01"
    data = c._create_blog_content(title, body, date, is_draft=True)
    response = c._post_request(data)
    print(response.text)
