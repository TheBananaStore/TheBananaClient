#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup


def get_long_description():
    with open("README.md") as file:
        return file.read()


setup(
    name="banana-client",
    version="1.0",
    description="Client for the Banana Store",
    long_description=get_long_description(),
    author="Alexey Pavlov",
    author_email="pezleha@gmail.com",
    maintainer="The Banana Team",
    maintainer_email="",
    url="https://thebananastore.cf",
    download_url="https://github.com/thebananastore/thebananaclient",
    install_requires=["os-release", "click"],
    classifiers=[
        # License
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        # Enviroment
        "Environment :: Other Environment",
        "Environment :: X11 Applications",
        "Environment :: X11 Applications :: Qt",
        # Operating system
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: Other",
        # Programming language
        "Programming Language :: Other",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        # Topics
        "Topic :: Desktop Environment",
        # Dev status
        "Development Status :: 1 - Planning",
    ],
    keywords="banana, store, thebananastore, bananaclient",
    packages=["banana_client"],
)
