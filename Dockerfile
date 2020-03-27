FROM python:3.6

COPY . /app

WORKDIR /app

RUN pip install flask gunicorn

EXPOSE 80

CMD [ "gunicorn", "-b 0.0.0.0:80", "--workers=2", "--threads=4", "--worker-class=gthread", "app:app" ]
