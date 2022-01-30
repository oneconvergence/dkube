# dkube
Repository for dkube sdk and libraries which can be used by client side applications to interface with Dkube platform.

Prerequisites
-------------
>=python3

sudo pip install -r requirements.txt or
sudo pip3 install -r requirements.txt


How to install using pip
------------------------
`sudo pip install  git+https://github.com/oneconvergence/dkube.git@2.2` or
`sudo pip3 install git+https://github.com/oneconvergence/dkube.git@2.2`


Kubeflow pipeline SDK
---------------------
DKube SDK no longer installs KFP SDK as part of this SDK installation. 

1. To install KFP SDK for DKube version 2.1.x/2.2.x

    `pip install kfp==1.4.0 kfp-server-api==1.2.0`

2. To install KFP SDK for DKube version 2.3.x+

    `pip install kfp==1.6.3 kfp-server-api==1.6.0`
