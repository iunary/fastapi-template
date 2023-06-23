FROM python:3.9-slim as builder
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt
# final stage
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*
RUN addgroup --system app && adduser --system --group app
USER app

COPY . /app
EXPOSE 8000
CMD [ "python", "/app/manage.py", "run" ]
