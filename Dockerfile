FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . .

EXPOSE 4444
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "4444"]
