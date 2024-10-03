
FROM python:3.9-slim

WORKDIR /app


COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV PYTHONUNBUFFERED=1

RUN python manage.py makemigrations 

RUN python manage.py migrate

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mangomail_app.wsgi:application"]