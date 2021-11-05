FROM python:3.10.0

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install poetry && poetry install --no-root

RUN poetry install
