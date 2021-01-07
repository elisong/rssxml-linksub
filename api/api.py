import re
from lxml import etree
import requests
from starlette.endpoints import HTTPEndpoint
from starlette.responses import Response


class Api(HTTPEndpoint):
    async def get(self, request):
        rss_url = request.query_params.get('rss')
        include_tags = request.query_params.get('tags')
        if rss_url:
            rss_xml = requests.get(rss_url).content
            root = etree.fromstring(rss_xml)
            resp_txt = treatment(root, include_tags)
            return Response(resp_txt, media_type='text/xml')
        else:
            return Response(
                'Failed, short of query parameter `rss`',
                status_code=400,
            )

    async def post(self, request):
        body = b''
        async for chunk in request.stream():
            body += chunk
        include_tags = request.query_params.get('tags')
        root = etree.fromstring(body)
        resp_txt = treatment(root, include_tags)
        return Response(resp_txt, media_type="text/xml")


def treatment(root, include_tags):
    for item in root.iter("item"):
        link_url = item.find("link").text
        description = item.find("description")
        tags = include_tags if include_tags else "img|a"
        description.text = re.sub(
            r'(<(?:%s)[^>]+(?:src|href)=[\"|\'])(?!https?:\/\/)([^\/].+?)([\"|\'])' % tags,
            r'\1' + link_url + r'\2\3',
            description.text
        )
    return etree.tostring(root, xml_declaration=True, encoding='utf-8', standalone=True)
