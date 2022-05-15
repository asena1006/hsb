

from .base import *


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)




# Take environment variables from .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.naver.com'
EMAIL_HOST_USER = 'hskanbu0501'
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_MAIL = 'hskanbu0501'