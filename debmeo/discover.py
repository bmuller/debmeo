import json
from bs4 import BeautifulSoup

from debmeo import io


def _parse_xml(xml):
    result = {}
    # bs4 can't handle a html child elem
    xml = xml.replace('<html>', '<content>')
    xml = xml.replace('</html>', '</content>')
    doc = BeautifulSoup(xml, "html.parser")
    for kid in doc.oembed.children:
        name = kid.name if kid.name != 'content' else 'html'
        result[name] = kid.text
    return result


def _parse_json(jsonstr):
    try:
        return json.loads(jsonstr)
    except ValueError:
        return None


async def get_embed(url):
    page = await io.get_page(url)
    if page is None:
        return None
    soup = BeautifulSoup(page, "html.parser")
    types = ('application/json+oembed', 'text/xml+oembed')
    link = soup.find('link', type=types, href=True)
    if link and link['type'] == 'application/json+oembed':
        parser = _parse_json
    elif link:
        parser = _parse_xml
    else:
        return None
    page = await io.get_page(link['href'])
    return parser(page) if page is not None else None
