FROM python:3.6

RUN apt install -y git
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/oneconvergence/dkube.git@pipeline --upgrade

ADD src/ /dkubepl
RUN python3 /dkubepl/main.py

