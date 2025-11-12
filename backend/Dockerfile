FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1  
WORKDIR /app

COPY requirements.txt ./

# 💡 Устанавливаем netcat перед pip install
RUN apt-get update && \
    apt-get install -y netcat-traditional && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . .
COPY .env .env
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["uvicorn","app.main:app","--host","0.0.0.0", "--port","8000", "--reload"]