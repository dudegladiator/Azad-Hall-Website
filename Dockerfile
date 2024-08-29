FROM python:3.8-alpine

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN apk --no-cache add build-base libffi-dev openssl-dev
RUN pip install -r requirements.txt

COPY ./azad_website /app
COPY .env /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
