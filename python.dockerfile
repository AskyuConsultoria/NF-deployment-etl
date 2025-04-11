FROM python:3.11-slim

WORKDIR /app

COPY req.txt ./

COPY . .

RUN pip install --no-cache-dir -r req.txt

ENTRYPOINT ["python", "main.py"]
