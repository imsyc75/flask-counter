FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY templates/ ./templates/

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /data

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["flask", "run", "--host=0.0.0.0"]