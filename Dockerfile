FROM python:3-alpine

RUN pip install cookiecutter

COPY . /app

WORKDIR /output

ENTRYPOINT cookiecutter --config-file cookiecutter_config.yml /app
