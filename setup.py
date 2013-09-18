# coding: utf-8

""" A Python module for NASA's Astrophysical Data Service (ADS) that doesn't suck. """

import re
import sys

try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

major, minor1, minor2, release, serial =  sys.version_info

readfile_kwargs = {"encoding": "utf-8"} if major >= 3 else {}

def readfile(filename):
    with open(filename, **readfile_kwargs) as fp:
        contents = fp.read()

    return contents

version_regex = re.compile("__version__ = \"(.*?)\"")
contents = readfile(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "ads",
    "__init__.py"))

version = version_regex.findall(contents)[0]

setup(name="ads",
      version=__version__,
      author="Andrew R. Casey",
      author_email="andy@the.astrowizici.st",
      packages=["ads"],
      url="http://www.github.com/andycasey/ads-python/",
      license="GPLv2",
      description="A Python module for NASA's ADS that doesn't suck.",
      long_description=readfile("README.md"),
      install_requires=[
        "requests",
        "requests_futures"
      ]
     )