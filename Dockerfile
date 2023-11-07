FROM python:3.10

COPY requirements.txt /tmp

WORKDIR /tmp

RUN pip install -r requirements.txt

ADD main.py .

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]

