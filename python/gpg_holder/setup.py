#!/usr/bin/env python3

__name__ = 'gpg_holder'
__version__ = '1.0'
__author__ = "Albert Szadziński"
__author_email__ = 'albert.szadzinski@pm.me'
__description__ = "Module to manage gpg keys"
__url__ = 'https://github.com/aszadzinski/scripts-notes-etc.git'
__license__ = 'MIT'

from setuptools import setup

with open('requirements.txt','r') as req:
    deps = req.read().splitlines()

setup(
        name = __name__,
        description = __description__,
        version = __version__,
        author = __author__,
        author_email = __author_email__,
        license = __license__,
        install_requires = deps,
        packages = ['gpg_holder'],
        )

