from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DJANGO_ENV = 'prod'
CITY = 'hz'
SECRET_KEY = ')&vb8g03g8g&hs=t+8@bf8qk#*42#2!%y#^ng=79$lf7*3q0h$'
DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hero_arithmetic_service',
    'rest_framework',
    'rest_framework_swagger',
    'django_apscheduler',
    'hero_hangzhou.traffic_tools',
    'hero_hangzhou.alarm_recommend',
    'hero_hangzhou.signal_control',
]

DATABASE_APPS_MAPPING = {
    'hero_arithmetic_service': 'default',
    'traffic_tools': 'default',
    'alarm_recommend': "default",
    'signal_control': "default",
    'admin': 'default',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=public'
        },
        'NAME': 'algorithm',  # 数据库名称
        'USER': 'dbuser',  # 拥有者，这个一般没修改
        'PASSWORD': 'l4exE4aP2NzYfyvlJY5lxQ',  # 密码，自己设定的
        'HOST': 'hz-hotdb1.dayu.com',  # 默认的就没写
        'PORT': '5432',
    },
}

ADCODE = 330100
