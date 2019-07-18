from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = false

ALLOWED_HOSTS = ['bolsadetrabajoescuela17.herokuapp.com']# Database

# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dejoh5rgc6cj1o',
        'USER': 'qfofywzmuhjrwm',
        'PASSWORD': 'f9e9badc4b9996ab8dce819c006b26c5f886c3b665a7c9e5a67c2808f3c0dae8',
        'HOST':'ec2-174-129-227-80.compute-1.amazonaws.com',
        'PORT':5432,
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)
