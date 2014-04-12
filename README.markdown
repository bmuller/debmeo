# debmeo: [oEmbed](http://oembed.com) for Python

This is yet another Python oEmbed library - but for [Python Twisted](http://twistedmatrix.com).

There is no caching of oembed URLs for services, only discovery is supported.  This means no list of URLs needs to be kept up to date.

## Installation

```
easy_install debmeo
```

## Usage
*This assumes you have a working familiarity with Twisted.*

Usage is pretty dang simple.

```python
from twisted.internet import reactor
from debmeo.discover import get_embed

def p(r):
    print r
    reactor.stop()

get_embed("https://twitter.com/bmuller/status/436965622082068481").addCallback(p)
reactor.run()
```

If the oEmbed data can be found, it will be returned as a dictionary.  If it can't be found, None will be given to the callback.

Easy peasy, and it's all asynchronous.
