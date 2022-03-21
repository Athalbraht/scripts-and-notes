from setuptools import setup

deps = ["click", "pandas", "matplotlib", "scipy"]

setup(
    name="DRSpy",
    description="Data loader for DRS4-psi",
    version="0.9",
    url="https://github.com/aszadzinski/scripts-and-notes/tree/master/python/DRS4-PSI",
    author="aszadzinski",
    license="MIT",
    requires=deps,
    install_requires=deps,
    packages=['DRSpy'],
    entry_points={
        'console_scripts': ['drspy = DRSpy:main']
    }
)

