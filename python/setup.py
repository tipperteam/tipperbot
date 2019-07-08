from setuptools import setup, find_packages

setup(
    name="tipperbot",
    version='0.0.1',
    packages=find_packages(exclude=["test*","jupiter","doc","src"]),
    install_requires=[],
    tests_require=[],
    package_data={
        '': ['*.txt', '*.rst', '*.md', '*.parquet'],
    },
    author="TipperTeam",
    author_email="",
    description="The original telegram TipperBot.",
    license="Proprietary",
    url="https://github.com/tipperteam/tipperbot",
)