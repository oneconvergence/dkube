#!/usr/bin/env python3

from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='dkube',
      version='2.1.4',
      description='Dkube SDK',
      author='oneconvergence',
      author_email='www.oneconvergence.com',
      url='git+https://github.com/oneconvergence/dkube.git',
      packages = find_packages(),
      install_requires=required,
      python_requires='>3.5'
     )
