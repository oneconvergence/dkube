FROM python:3.5.4

RUN apt install -y git
RUN pip install git+https://github.com/oneconvergence/dkube.git@dev --upgrade
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p /opt/dkube/

COPY bin/* /opt/dkube/

ENV PATH="/opt/dkube/:${PATH}"
