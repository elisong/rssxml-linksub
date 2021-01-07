# RSS XML Link Substitution - Python Api

## Try online app

- https://rssxml-linksub.herokuapp.com

## Simple case（python `Requests` client for example）

```python
# GET
from os.path import join
import requests

resp = requests.get(
    "https://rssxml-linksub.herokuapp.com/api/?"
    "rss=https://rssxml-linksub.herokuapp.com/static/demo.xml"
)
assert resp.status_code == 200
assert resp.headers["Content-Type"] == "text/xml; charset=utf-8"
print(resp.text)
```

```python
# POST
from os.path import join
from lxml import etree
import requests

tree = etree.parse(join("static", "demo.xml"))
root = tree.getroot()
resp = requests.post(
    "http://127.0.0.1:8000/api/",
    headers={"Content-Type": "application/xml"},
    data=etree.tostring(root, encoding='utf-8')
)
assert resp.status_code == 200
assert resp.headers["Content-Type"] == "text/xml; charset=utf-8"
print(resp.text)
```

## Dependencies

- Python-3.7.9
- `requirements.txt`

> More about xml parser choosen: At very beginning, I choose `defusedxml.ElementTree` (a wrapper over xml.etree.ElementTree for more security), but it always loss xml declaration when using `xml.etree.ElementTree.tostring()` to export. According to [documents](https://docs.python.org/3/library/xml.etree.elementtree.html), `xml.etree.ElementTree.tostring(..., xml_declaration=xxx)` only valid after python >= 3.8. Bitterly, platform like Heroku, vercel.com offer defaut python runtime < 3.8. So finally choose `lxml`.

## Deployment

- [Heroku - getting-started-with-python](https://devcenter.heroku.com/articles/getting-started-with-python)
  - runtime.txt
  - Procfile
