FROM python:3.10

ADD main.py .

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]

