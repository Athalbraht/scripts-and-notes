from setuptools import setup

deps = ["numpy"]

setup(
    name="NeuralPy",
    description="Simple forward neural network ",
    version="v0.1",
    author="Albert Szadziński",
    author_email="albert.szadzinski@smcebi.edu.pl",
    install_requires=deps,
    license="MIT",
    packages=['NeuralPy'],
)
