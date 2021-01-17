FROM python:3.6

RUN apt install -y git
COPY launcher/requirements.txt .
RUN pip install -r requirements.txt
ADD dist /dist
RUN pip install /dist/*.whl

ADD launcher/src/ /dkubepl
RUN python3 /dkubepl/main.py

