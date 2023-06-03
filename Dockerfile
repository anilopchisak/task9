FROM python:3.10.2

COPY . /opt/app

WORKDIR /opt/app

LABEL authors="polinakasich"

CMD ["pyhton", "manage.py", "runserver", "0:8000"]