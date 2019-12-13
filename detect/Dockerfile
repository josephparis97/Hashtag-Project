FROM python:3.7-slim-stretch

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./src .

CMD [ "python", "app.py" ]