#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='mpltex',
        version='0.1.0',
        author='Will Vousden',
        author_email='will@vousden.me.uk',
        license='MIT',
        keywords=['latex', 'tex', 'mpl', 'matplotlib', 'plotting', 'plot'],
        packages=find_packages(exclude=['docs', 'tests*']),
        url='https://github.com/willvousden/mpltex',
        description='Utility for plotting for LaTeX from Matplotlib.',
        long_description='',
        install_requires=['matplotlib']
)
