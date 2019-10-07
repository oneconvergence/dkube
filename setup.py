#!/usr/bin/env python3

from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='dkube',
      version='0.1',
      description='Dkube SDK',
      author='oneconvergence',
      author_email='www.oneconvergence.com',
      url='git+https://github.com/oneconvergence/dkube.git',
      packages = ['dkube', 'dkube.sdk', 'dkube.sdk.env', 'dkube.sdk.rest', 'dkube.sdk.schema'],
      install_requires=required
     )
