FROM python:3.10-slim as base

ENV PYTHONPATH /microservices
ENV POETRY_VIRTUALENVS_CREATE false

RUN apt-get update && apt-get install -qq -y \
    build-essential libpq-dev netcat --no-install-recommends

WORKDIR /microservices/

RUN pip install --upgrade pip && pip install poetry

COPY poetry.lock pyproject.toml /microservices/

RUN poetry install

COPY bot/ /microservices/