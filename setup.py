#!/usr/bin/env python3

import os

from setuptools import setup

from kph import __version__


def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
  name = "kph",
  version = __version__,
  url = "https://github.com/mherrmann/kph",
  license = "GPL-3",
  description = "Python 2/3 ready implementation of the Koelner Phonetic.",
  long_description = read("README"),
  author = "Robert Schindler",
  author_email = "r.schindler@efficiosoft.com",
  packages = ["kph"],
  classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Natural Language :: English',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Software Development :: Libraries :: Python Modules',
  ]
)
