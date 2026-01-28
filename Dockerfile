FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY pyproject.toml README.md /app/
COPY src /app/src

RUN pip install --no-cache-dir -e .

CMD ["python", "-m", "news_summary.cli", "Report/Reiner-AI-信息差-2026-01-28.html"]
