FROM python:3.7-slim

RUN apt-get update && \
    apt-get install -y \
        gettext \
        make && \
    apt-get clean && \
    rm -rf /var/cache/apt && \
    pip install pipenv

WORKDIR /app
ARG PIPENV_FLAGS="--deploy --system"

COPY Makefile Pipfile Pipfile.lock /app/
RUN make init

COPY . /app

CMD make run -j 5
