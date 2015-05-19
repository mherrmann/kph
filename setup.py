#!/usr/bin/env python


import os

from setuptools import setup, find_packages


def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
  name = "kph",
  version = "0.3",
  url = "https://github.com/mherrmann/kph",
  license = "GPL-3",
  description = "An easy implementation of the Koelner Phonetic.",
  long_description = read("README"),
  author = "Robert Schindler",
  author_email = "robert-sch@gmx.net",
  packages = find_packages("src"),
  package_dir = {"": "src"},
  install_requires= ["setuptools"],
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
