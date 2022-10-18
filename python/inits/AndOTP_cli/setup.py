#!/usr/bin/env python3

from setuptools import setup
import andOTP_cli

deps = [ ]

setup(
        name = andOTP_cli.__name__,
        description = andOTP_cli.__description__,
        version = andOTP_cli.__version__,
        author = andOTP_cli.__author__,
        author_email = andOTP_cli.__author_email__,
        license = andOTP_cli.__license__,
        requires = deps,
        install_requires = deps,
        packages = ['andOTP_cli'],
        entry_points = {
            'console_scripts': ['andOTP_cli = andOTP_cli.andOTP:main']
                        }
        )
