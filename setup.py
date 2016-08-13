#!/usr/bin/env python
from setuptools import setup, find_packages
import debmeo

setup(
    name="debmeo",
    version=debmeo.__version__,
    description="Get oEmbed info asynchronously",
    author="Brian Muller",
    author_email="bamuller@gmail.com",
    license="MIT",
    url="http://github.com/bmuller/debmeo",
    packages=find_packages(),
    install_requires=["aiohttp>=0.22.5", "beautifulsoup4>=4.5.1"],
    scripts=['bin/debmeo']
)
