FROM python:3.8-alpine

COPY requirements.txt /requirements.txt
COPY main.py /main.py

ENV PATH "$PATH:/home/root/.npm-global/bin"

RUN python -m pip install --upgrade pip wheel setuptools
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/main.py"]