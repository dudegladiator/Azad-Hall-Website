#!bin/sh

if [ -f .env ]; then
    set -a
    . ./.env
    set +a
fi

echo "Path of all commands: $PATH"
python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py createsuperuserwithpassword --username harsh90731 --password letmelogin --email gladiator098123@gmail.com --preserve
python manage.py loaddata initial_data

gunicorn azad_website.wsgi:application --bind 0.0.0.0:9000
