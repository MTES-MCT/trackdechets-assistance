# Run web app
web: gunicorn --chdir src config.wsgi:application --log-file -

postdeploy: python src/manage.py migrate