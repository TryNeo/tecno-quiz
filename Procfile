release: python manage.py migrate
release: heroku config:set DISABLE_COLLECTSTATIC=1
web: gunicorn TecnoQuiz.wsgi --log-file -