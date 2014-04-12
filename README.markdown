# debmeo: [oEmbed](http://oembed.com) for Python

This is yet another [Python oEmbed library](https://pypi.python.org/pypi?%3Aaction=search&term=oembed&submit=search) - but for [Python Twisted](http://twistedmatrix.com).

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

which will poop out:

```python
{
    u'provider_url': u'https://twitter.com',
    u'url': u'https://twitter.com/bmuller/statuses/436965622082068481',
    u'html': u'<blockquote class="twitter-tweet"><p>&quot;So You Think You Found a Technical Co-founder&quot; - a list of questions to ask yourself and them - <a href="http://t.co/ALixRKwk8e">http://t.co/ALixRKwk8e</a></p>&mdash; bmuller (@bmuller) <a href="https://twitter.com/bmuller/statuses/436965622082068481">February 21, 2014</a></blockquote>\n<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>',
    u'author_name': u'bmuller',
    u'height': None,
    u'width': 550,
    u'version': u'1.0',
    u'author_url': u'https://twitter.com/bmuller',
    u'provider_name': u'Twitter',
    u'cache_age': u'3153600000',
    u'type': u'rich'
}
```

If the oEmbed data can be found, it will be returned as a dictionary.  If it can't be found, None will be given to the callback.

Easy peasy, and it's all asynchronous.
