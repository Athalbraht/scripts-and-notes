from setuptools import setup

deps = []

setup(
    name="macc",
    description="MAC changer script",
    version="v1.0",
    author="Albert Szadziński",
    author_email="albert.szadzinski@pm.me",
    license="MIT",
    install_requires=deps,
    packages=['macc'],
    entry_points={
        'console_scripts': ['macc = macc.macc:main']
    }
)
