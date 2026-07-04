ARG PYTHON_VERSION=3.14

FROM python:${PYTHON_VERSION}

RUN pip install uv

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .
RUN uv sync --frozen
RUN ln -s /app/.venv/bin/uvicorn /usr/local/bin/uvicorn

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
