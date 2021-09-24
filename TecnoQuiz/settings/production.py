import dj_database_url
from decouple import config

DEBUG = False

ALLOWED_HOSTS = ['tecno-quiz.herokuapp.com']


DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('USUARIO_CORREO')
EMAIL_HOST_PASSWORD =config('CONTRA_EMAIL')