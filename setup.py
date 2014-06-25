#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
        name='MplTex',
        version='0.1.0',
        author='Will Vousden',
        author_email='will@vousden.me.uk',
        packages=['mpltex', 'mpltex.tests'],
        url='https://github.com/willvousden/mpltex',
        description='Utility for plotting for LaTeX from Matplotlib.',
        license='',
        long_description='',
        install_requires=['matplotlib']
)
