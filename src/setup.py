import os
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pymake3",
    version="0.0.1",
    author="Shlomi Matichin",
    author_email="shlomomatichin@gmail.com",
    description=(
        "Pymake3 is python3 port of pymake2. it provides automated build tasks and enormous flexibility, all without esoteric syntax constructs!"),
    packages=[
            'pymake3',
            'pymake3.utils',
            'pymake3.cli',
            'pymake3.core',
            'pymake3.makeutils',
            'pymake3.template',
            'pymake3.template.util',
            'pymake3.template.c',
            'pymake3.template.csharp',
            'pymake3.template.latex',
            ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shlomimatichin/Pymake3",
)
