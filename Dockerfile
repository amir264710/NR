FROM python:3.10

COPY requirements.txt .

WORKDIR /NR

ADD main.py .

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]

