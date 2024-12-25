FROM python:3.8-alpine

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN apk --no-cache add build-base libffi-dev openssl-dev mariadb-dev
RUN pip install -r requirements.txt

COPY ./azad_website /app

# Create default .env file if not exists
RUN echo '#!/bin/sh\n\
if [ ! -f /app/.env ]; then\n\
    echo "Creating default .env file"\n\
    cat > /app/.env << EOL\n\
EOL\n\
else\n\
    echo ".env file exists, using existing file"\n\
fi' > /app/create_env.sh

RUN chmod +x /app/create_env.sh

#WORKDIR /app

COPY /entrypoint.sh /
# Modify entrypoint.sh to run create_env.sh first
RUN sed -i '1i/app/create_env.sh' /entrypoint.sh

EXPOSE 10000

ENTRYPOINT ["sh", "/entrypoint.sh"]