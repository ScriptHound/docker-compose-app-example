FROM python:3.10-slim

COPY . .
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

WORKDIR /app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
