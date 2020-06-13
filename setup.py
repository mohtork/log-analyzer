# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup

setup(name='LogAnalyzer',
      version='0.1',
      description='Log Analyzer Tool',
      url='https://github.com/mohtork/log-analyzer',
      author='Torkey',
      author_email='',
      setup_requires='setuptools',
      package_dir={'': 'loganalyzer'},
      packages=find_packages(where='loganalyzer'),
      license='Apache 2.0',
      zip_safe=False)
