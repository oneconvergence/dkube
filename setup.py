#!/usr/bin/env python3

from distutils.core import setup

setup(name='dkube',
      version='1.0',
      description='Python Distribution Utilities',
      author='ahmed.khan',
      author_email='ahmed.khan@oneconvergence.com',
      url='git+https://github.com/mak-454/dkube.git',
      packages = ['dkube', 'dkube.sdk', 'dkube.sdk.env', 'dkube.sdk.rest', 'dkube.sdk.schema']
     )
