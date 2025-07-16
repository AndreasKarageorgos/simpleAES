from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    description = readme.read()

setup(
    name="simple-aes",
    author="Andreas Karageorgos",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pycryptodome"
    ],
    license="MIT",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/AndreasKarageorgos/simpleAES"
)