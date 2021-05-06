FROM python:3.8.5


RUN apt install -y git
RUN pip install git+https://github.com/oneconvergence/dkube.git@slurmdemo --upgrade
COPY requirements.txt .
RUN pip install -r requirements.txt
