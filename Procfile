# Run web app
web: gunicorn --chdir src config.wsgi:application --log-file -


# post-deploy tasks
postdeploy: bash src/bin/post_deploy
