#!/usr/bin/env python3

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="dkube",
    version="3.7",
    description="Dkube SDK",
    author="oneconvergence",
    author_email="dkube@oneconvergence.com",
    url="https://github.com/oneconvergence/dkube.git",
    packages=find_packages(),
    install_requires=required,
    python_requires=">3.5",
)
