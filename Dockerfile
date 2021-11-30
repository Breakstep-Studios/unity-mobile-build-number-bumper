FROM python:3.8-alpine

ADD requirements.txt /requirements.txt
ADD main.py /main.py

RUN python -m pip install --upgrade pip wheel setuptools
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/main.py"]