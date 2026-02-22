FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3232

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3232"]