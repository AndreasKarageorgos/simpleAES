from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    description = readme.read()

setup(
    name="pycryptosimple_aes",
    author="Andreas Karageorgos",
    version="1.1",
    packages=find_packages(),
    install_requires=[
        "pycryptodome"
    ],
    license="MIT",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/AndreasKarageorgos/simpleAES"
)