import json
from bs4 import BeautifulSoup

from debmeo import io


def get_embed(url):
    return Fetcher(url).get_embed()


class Fetcher:
    def __init__(self, url):
        self.url = url

    def parse_xml(self, xml):
        result = {}
        # bs4 can't handle a html child elem
        xml = xml.replace('<html>', '<content>')
        xml = xml.replace('</html>', '</content>')
        doc = BeautifulSoup(xml, "html.parser")
        for kid in doc.oembed.children:
            name = kid.name if kid.name != 'content' else 'html'
            result[name] = kid.text
        return result

    def parse_json(self, jsonstr):
        try:
            return json.loads(jsonstr)
        except:
            return None

    async def get_embed(self):
        page = await io.getPage(self.url)
        if page is None:
            return None
        soup = BeautifulSoup(page, "html.parser")
        types = ('application/json+oembed', 'text/xml+oembed')
        link = soup.find('link', type=types, href=True)
        if link and link['type'] == 'application/json+oembed':
            parser = self.parse_json
        elif link:
            parser = self.parse_xml
        else:
            return None
        page = await io.getPage(link['href'])
        return parser(page) if page is not None else None
