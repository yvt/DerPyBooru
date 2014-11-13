#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

import derpibooru

setup(
  name = "DerPyBooru",
  description = "Python bindings for Derpibooru's API",
  url = "https://github.com/joshua-stone/DerPyBooru",
  version = "0.4",
  author = "Joshua Stone",
  license = "Simplified BSD License",
  platforms = ["any"],
  packages = find_packages(),
  install_requires = ["requests"],
  include_package_data = True,
  classifiers = [
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Simplified BSD License",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Internet"
  ]
)
