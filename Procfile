release: python manage.py migrate && python manage.py seed
web: gunicorn wellth_water.wsgi --log-file -
