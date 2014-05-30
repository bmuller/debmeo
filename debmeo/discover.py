import json
from twisted.internet import defer
from bs4 import BeautifulSoup

from debmeo import io


def get_embed(url):
    return Fetcher(url).get_embed()


class Fetcher(object):
    def __init__(self, url):
        self.url = url

    def parse_xml(self, xml):
        result = {}
        # bs4 can't handle a html child elem
        xml = xml.replace('<html>', '<content>').replace('</html>', '</content>')
        doc = BeautifulSoup(xml)
        for kid in doc.oembed.children:
            name = kid.name if kid.name != 'content' else 'html'
            result[name] = kid.text
        return result

    def parse_json(self, json):
        result = None
        try:
            result = json.loads(json)
        except:
            pass
        return result

    def extract_link(self, response):
        soup = BeautifulSoup(response.body)
        types = ('application/json+oembed', 'text/xml+oembed')
        link = soup.find('link', type=types, href=True)
        if link and link['type'] == 'application/json+oembed':
            parser = self.parse_json
        elif link:
            parser = self.parse_xml
        else:
            return defer.succeed(None)
        return io.getPage(link['href']).addCallbacks(lambda r: parser(r.body) if r.body else None, self.failure)

    def get_embed(self):
        return io.getPage(self.url).addCallbacks(self.extract_link, self.failure)

    def failure(self, error):
        return None
