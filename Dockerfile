FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY init_db.sh .
RUN chmod +x init_db.sh

EXPOSE 3232

CMD ["sh", "init_db.sh", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3232"]
