from twisted.web.http import PotentialDataLoss
import treq

class Collector:
    def __init__(self):
        self.body = ""

    def start(self, resp):
        self.resp = resp
        return treq.collect(self.resp, self.collect)

    def collect(self, data):
        self.body += data
        if len(self.body) > 300000:
            raise PotentialDataLoss

def getPage(url):
    agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 "
    agent += "(KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36"
    if isinstance(url, unicode):
        url = url.encode('ascii', errors='ignore')
    collector = Collector()
    d = treq.get(url, headers={'User-Agent': agent}, timeout=10)
    d.addCallback(collector.start)
    return d.addCallback(lambda _: collector)
