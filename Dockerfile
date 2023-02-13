FROM python:3

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8002

CMD ["gunicorn", "--bind", "0.0.0.0:8002", "wsgi:app"]