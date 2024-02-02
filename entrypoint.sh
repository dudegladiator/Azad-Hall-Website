#!bin/sh

echo "Path of all commands: $PATH"
python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py createsuperuserwithpassword --username <username> --password <password> --email <email> --preserve
python manage.py loaddata initial_data

gunicorn azad_website.wsgi:application --bind 0.0.0.0:8000
