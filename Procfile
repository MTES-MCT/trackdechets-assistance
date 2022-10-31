# Run web app
web: gunicorn --chdir src config.wsgi:application --log-file -

postdeploy: python manage.py migrate