FROM python:3.10-alpine
LABEL author="baclrary"

ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev libffi-dev zlib zlib-dev

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

RUN adduser --disabled-password --no-create-home django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol

USER django-user
