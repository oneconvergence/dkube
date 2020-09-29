.. contents:: Table of Contents
    :depth: 2
    :local:

.. role:: bash(code)
   :language: bash

DKube SDK Developer Guide
**************************

The document is guide for developers to build ML applications on DKube platform.
DKube SDK is repository of abstract python classes and libraries which can be used by client side applications to interface with Dkube platform.


How to install
==============
Python >=python3.5 is required

Install using *pip* from *git* using below command::

    sudo pip install git+https://github.com/oneconvergence/dkube.git or
    sudo pip3 install git+https://github.com/oneconvergence/dkube.git


It will install all the prerequisites in *requirements.txt*

SDK API
=======
.. automodule:: dkube.sdk.api
    :members:

DKube API Swagger Spec
======================
- Full spec of DKube APIs
- All the code is under package `dkube.sdk.internal.dkube_api`


Click the link to view spec `DKUBEAPI`_.

.. _DKUBEAPI: apidoc/index.html


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
