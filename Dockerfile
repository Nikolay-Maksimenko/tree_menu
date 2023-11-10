FROM python:3.11

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app/
WORKDIR /app/

COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
