from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DJANGO_ENV = 'dev'
CITY = 'hz'
SECRET_KEY = ')&vb8g03g8g&hs=t+8@bf8qk#*42#2!%y#^ng=79$lf7*3q0h$'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_manage',
    'django_apscheduler',
    'apple',
]

DATABASE_APPS_MAPPING = {
    'admin': 'default',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=public'
        },
        'NAME': 'alg',  # 数据库名称
        'USER': 'django',  # 拥有者，这个一般没修改
        'PASSWORD': 'django',  # 密码，自己设定的
        'HOST': '192.168.22.70',  # 默认的就没写
        'PORT': '5432',
    },
}

ADCODE = 330100
