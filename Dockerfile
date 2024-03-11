FROM python:3.11-slim-buster

ENV YOUR_ENV=production \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # Poetry's configuration:
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.7.1
  # ^^^
  # needs to match poetry-core's version on pyproject.toml

# System deps:
# RUN curl -sSL https://install.python-poetry.org | python3 -
RUN pip install poetry==1.7.1


# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# EXPOSE 5000
# Project initialization:
RUN poetry install --only=main --no-interaction --no-ansi --no-root

# Creating folders, and files for a project:
COPY . /code

CMD ["gunicorn", "wsgi:application", "--workers=2", "--threads=2", "--bind=0.0.0.0:5000"]
