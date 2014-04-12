#!/usr/bin/env python
from setuptools import setup, find_packages
from rpcudp import version

setup(
    name="debmeo",
    version=version,
    description="Get oEmbed info asynchronously",
    author="Brian Muller",
    author_email="bamuller@gmail.com",
    license="MIT",
    url="http://github.com/bmuller/debmeo",
    packages=find_packages(),
    requires=["twisted.internet", "bs4"],
    install_requires=['twisted>=12.0', "beautifulsoup4>=4.3.0"]
)
