from twisted.web.client import HTTPClientFactory, _makeGetterFactory, HTTPPageGetter

import zlib


class HTTPPageGetterModifiable(HTTPPageGetter):
    def lineReceived(self, line):
        """
        Make sure we don't download anything too big...
        """
        if not hasattr(self, '_totalSize'):
            self._totalSize = 0
        self._totalSize += len(line)
        if self._totalSize > 300000:
            self.timeout()
        return HTTPPageGetter.lineReceived(self, line)

    def handleStatus_304(self):
        pass


class DebmeoHTTPClientFactory(HTTPClientFactory):
    protocol = HTTPPageGetterModifiable

    def gotHeaders(self, headers):
        """
        make HTTPClientFactory a bit more robust when cookie headers
        are a bit f'ed
        """
        try:
            HTTPClientFactory.gotHeaders(self, headers)
        except ValueError:
            pass

    def page(self, body):
        if self.waiting:
            self.waiting = 0
            if 'gzip' in self.response_headers.get('content-encoding', []):
                zlibDecompress = zlib.decompressobj(16 + zlib.MAX_WBITS)
                body = zlibDecompress.decompress(body)
            self.body = body
            self.deferred.callback(self)


def getPage(url):
    agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 "
    agent += "(KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36"
    if isinstance(url, unicode):
        url = url.encode('ascii', errors='ignore')
    return _makeGetterFactory(url, DebmeoHTTPClientFactory, agent=agent, timeout=10).deferred
