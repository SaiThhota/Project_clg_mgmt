python manage.py migrate
python manage.py collectstatic --noinput
gunicorn Clg_administration.wsgi:application