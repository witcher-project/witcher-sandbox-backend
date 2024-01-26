FROM python:3.10-alpine
LABEL author="baclrary"

ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev libffi-dev

RUN pip install --upgrade pip && \
    pip install poetry

WORKDIR /app

COPY ./pyproject.toml /app/pyproject.toml
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY ./app /app

RUN apk del .tmp-build-deps && \
    rm -rf /tmp

EXPOSE 8000

RUN adduser --disabled-password --no-create-home django-user
USER django-user
