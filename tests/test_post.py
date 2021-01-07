from os.path import join
from lxml import etree
import requests


def test_post_success():
    tree = etree.parse(join("static", "demo.xml"))
    root = tree.getroot()
    resp = requests.post(
        "http://127.0.0.1:8000/api/",
        headers={"Content-Type": "application/xml"},
        data=etree.tostring(root, encoding='utf-8')
    )
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "text/xml; charset=utf-8"
