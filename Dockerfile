FROM python:3.11

WORKDIR /app

RUN pip install --upgrade pip
COPY  requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
