"""
Django settings for treval project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import random
import sys
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0,os.path.join(BASE_DIR,"apps"))
sys.path.insert(1, os.path.join(BASE_DIR, 'lib'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@0f-l^zn7l&qw!&+yc1ejkaw0vtt*$v8pr(-rmof1k@o^)g%5g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'xadmin',
    'crispy_forms',
    'DjangoUeditor',
    'captcha',

    'rest_framework',

    'users',
    'diarys',
    'news',
    'operation',
    'scenicspots',
    'shop',
    'pay',
'rest_framework.authtoken',

]



AUTH_USER_MODEL = 'users.MyUser'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'treval.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',

            ],
        },
    },
]

WSGI_APPLICATION = 'treval.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel2',
        'USER': "root",
        "PORT":"3306",
        'PASSWORD': "916149",
        'HOST': "localhost",

    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,  'static').replace('\\','/')
STATICFILES_DIRS  =(
    ("css", os.path.join(STATIC_ROOT,'css').replace('\\','/')),
    ("js", os.path.join(STATIC_ROOT,'js').replace('\\','/')),
('images',os.path.join(STATIC_ROOT,'images').replace('\\','/') ),
('fonts',os.path.join(STATIC_ROOT,'fonts').replace('\\','/') ),

)


# 处理静态文件
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_DIRS = (
    os.path.join(BASE_DIR, 'media')
)











# 验证码的设置
CAPTCHA_IMAGE_SIZE = (100,30)  #设置生成验证码图片的长和宽，单位为像素
CAPTCHA_OUTPUT_FORMAT = u'%(text_field)s %(image)s %(hidden_field)s' #设置输出的格式，该插件自动在模板中生成3个元素：一个验证码图片，一个验证码输入框、一个用于存放秘钥的隐藏输入框。可以在此根据需要调整其在模板中生成的先后顺序
CAPTCHA_FOREGROUND_COLOR = (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))  #设置验证码图片前景色
CAPTCHA_BACKGROUND_COLOR = '#ffffff'  #设置验证码图片背景色
CAPTCHA_FONT_SIZE = 30   #设置验证码图片中字体大小
CAPTCHA_FONT_PATH = 'C:\Windows\Fonts\Arial\\arial.ttf'   #设置字体样式，支持TTF等文件格式
CAPTCHA_LETTER_ROTATION = (-35,35)  #设置验证码中字母旋转的角度
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_arcs','captcha.helpers.noise_dots',)  #是否添加干扰点和干扰线，当值为'captcha.helpers.noise_null'时，表示不添加干扰
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_TIMEOUT = '5' #设置验证码的有效时间，单位为分钟
CAPTCHA_LENGTH = '4' #当验证码类型为字符型时，指定字母个数




EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS= False
EMAIL_FROM = ''


# 支付宝设置
ALIPAY_APPID = 'appidappidappidappidappid'
# 公钥
ALIPAY_PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'apps/pay/keys/alipay_public_key')
# 私钥
APP_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'apps/pay/keys/alipay_app_private_key')
# 接口
ALIPAY_URL = 'https://openapi.alipaydev.com/gateway.do?'
# 支付关闭时间：
ALIPAY_CLOSE_TIME = '60m'

DOMAIN_NAME = 'http://127.0.0.1:8080/'






REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',

    ),
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
#     JWT_EXPIRATION_DELTA 指明token的有效期
}
