from setuptools import setup

deps = ["click", "pandas", "matplotlib", "scipy"]

setup(
    name="DRSpy",
    description="Data loader for DRS4-psi",
    version="1.0",
    author="Albert Szadziński",
    license="MIT",
    requires=deps,
    install_requires=deps,
    packages=['DRSpy'],
    entry_points={
        'console_scripts': ['drspy = DRSpy:main']
    }
)

