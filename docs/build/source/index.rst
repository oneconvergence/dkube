.. role:: bash(code)
   :language: bash

.. |br| raw:: html

   <br />

DKube SDK Developer Guide
**************************

The document is guide for developers to build ML applications on DKube platform.
DKube SDK is repository of abstract python classes and libraries which can be used by client side applications to interface with Dkube platform.


How to install
==============
Python >=python3.5 is required

Install using *pip* from *git* using below command::

    sudo pip install git+https://github.com/oneconvergence/dkube.git@2.2 or
    sudo pip3 install git+https://github.com/oneconvergence/dkube.git@2.2


It will install all the prerequisites in *requirements.txt*

SDK API
=======
.. automodule:: dkube.sdk.api
    :members:

DKube Resources
===============
.. automodule:: dkube.sdk.rsrcs.project
    :members:

.. automodule:: dkube.sdk.rsrcs.dataset
    :members:

.. automodule:: dkube.sdk.rsrcs.code
    :members:

.. automodule:: dkube.sdk.rsrcs.featureset
    :members:

.. automodule:: dkube.sdk.rsrcs.model
    :members:

.. automodule:: dkube.sdk.rsrcs.training
    :members:

.. automodule:: dkube.sdk.rsrcs.preprocessing
    :members:

.. automodule:: dkube.sdk.rsrcs.ide
    :members:

.. automodule:: dkube.sdk.rsrcs.serving
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
