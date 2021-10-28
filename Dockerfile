FROM python:3.7.2

RUN pip install pipenv

ADD . /subway-usage

WORKDIR /subway-usage

RUN pipenv install --system --skip-lock

RUN pip install gunicorn[gevent]

EXPOSE 5000