# Project Chimera — Reproducible Dev/Test Environment
FROM python:3.11-slim

# Prevent Python from writing pyc files & buffering logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# System dependencies (minimal)
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
 && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
# (tests only, no runtime logic yet)
RUN pip install --upgrade pip \
 && pip install pytest

# Default command
CMD ["pytest", "-q"]
