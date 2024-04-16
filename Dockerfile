# syntax=docker/dockerfile:1

# Use the official Python image as the base image.
# You can specify the desired Python version with the PYTHON_VERSION argument.
ARG PYTHON_VERSION=3.11.3
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Install poetry
RUN pip install poetry

# Set the working directory in the container.
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files into the container.
COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false --local

# Install dependencies using Poetry.
RUN poetry config virtualenvs.path /venv \
    && poetry install --no-root --no-interaction --no-ansi --no-cache

# Copy the source code into the container.
COPY . /app/

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application using Poetry.
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
