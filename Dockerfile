FROM python:3.13-slim

WORKDIR /app

RUN pip install poetry==2.1.3

ENV PATH="/app/src:$PATH" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.lock ./
RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

WORKDIR /app/src

EXPOSE 8000

CMD [""]