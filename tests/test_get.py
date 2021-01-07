from os.path import join
import requests

# need start local server


def test_get_success():
    resp = requests.get(
        "http://localhost:8000/api/?"
        "rss=https://rssxml-linksub.herokuapp.com/static/demo.xml"
    )
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "text/xml; charset=utf-8"
