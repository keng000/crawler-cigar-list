from cuban.base.utils.announcements.blog import HatenaController


def test_create_blog_content():
    c = HatenaController()

    title = "test_title"
    body = "test_body"
    date = "2010-01-01"
    data = c._create_blog_content(title, body, date, is_draft=False)

    ans = """<?xml version="1.0" encoding="utf-8"?>
<entry xmlns="http://www.w3.org/2005/Atom"
       xmlns:app="http://www.w3.org/2007/app">
  <title>test_title</title>
  <author><name>keng000</name></author>
  <content type="text/x-markdown">test_body</content>
  <updated>2010-01-01T01:00:00+09:00</updated>
  <app:control>
    <app:draft>no</app:draft>
  </app:control>
</entry>
""".encode()
    assert data == ans


def test_create_blog_content_draft():
    c = HatenaController()

    title = "test_title"
    body = "test_body"
    date = "2010-01-01"
    data = c._create_blog_content(title, body, date, is_draft=True)

    ans = """<?xml version="1.0" encoding="utf-8"?>
<entry xmlns="http://www.w3.org/2005/Atom"
       xmlns:app="http://www.w3.org/2007/app">
  <title>test_title</title>
  <author><name>keng000</name></author>
  <content type="text/x-markdown">test_body</content>
  <updated>2010-01-01T01:00:00+09:00</updated>
  <app:control>
    <app:draft>yes</app:draft>
  </app:control>
</entry>
""".encode()
    assert data == ans


# def test_post():
#     c = HatenaController()
#
#     title = "test_title"
#     body = "test_body"
#     date = "2010-01-01"
#     data = c._create_blog_content(title, body, date, is_draft=True)
#     response = c._post_request(data)
#     print(response)
