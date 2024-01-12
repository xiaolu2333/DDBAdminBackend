"""
Django settings for DDBAdminBackend project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
# from Crypto import Random
# from Crypto.PublicKey import RSA

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+3jl%!er_wk!&j1tc5_2uwbtaxa-3)(85-r4he%^s82ap_6t^t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'framework.login',
    'framework.authentication',
    'framework.organizations',
    'framework.departments',
    'framework.resources',
    'framework.dictionaries',
    'framework.strategies',
    'test_app',
    'data_management.data_tree_manage',
    'data_management.database_manage',
    'data_service.erd_service',
    'learn',

    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DDBAdminBackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DDBAdminBackend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # # 使用 sqlite3 数据库
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    # 使用 postgresql 数据库
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DDBAdmin',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static uploadfiles (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 允许跨域
CORS_ORIGIN_ALLOW_ALL = True  # 允许所有域名跨域
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie
CORS_ORIGIN_WHITELIST = (
    'http://localhost:5173',
)  # 允许跨域的域名
CORS_ALLOW_METHODS = (  # 允许的请求方法
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
    'VIEW',
)
# 允许的请求头
CORS_ALLOW_HEADERS = (
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-requested-with',
    'x-csrftoken',
    'X_FILENAME',
    'XMLHttpRequest',
    'content-range',
    'range',
)
# 允许的响应头
CORS_EXPOSE_HEADERS = (
    'range',
    'content-range',
    'content-length',
    'content-type',
    'content-disposition',
)

# 文件上传大小限制
DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 1024  # 1G
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 1024  # 1G

# # 自定义用户模型
# AUTH_USER_MODEL = 'authentication.CustomUser'

# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.primitives.asymmetric import rsa
#
# # 生成RSA密钥对
# PRIVATE_KEY = rsa.generate_private_key(
#     public_exponent=65537,
#     key_size=2048,
# )
#
# # 获取私钥的PEM格式
# private_pem = PRIVATE_KEY.private_bytes(
#     encoding=serialization.Encoding.PEM,
#     format=serialization.PrivateFormat.PKCS8,
#     encryption_algorithm=serialization.NoEncryption()
# )
#
# # 将私钥保存到文件
# with open('private_key.pem', 'wb') as f:
#     f.write(private_pem)
#
# # 获取公钥的PEM格式
# PUBLIC_KEY = PRIVATE_KEY.public_key()
# public_pem = PUBLIC_KEY.public_bytes(
#     encoding=serialization.Encoding.PEM,
#     format=serialization.PublicFormat.SubjectPublicKeyInfo
# )
#
# # 将公钥保存到文件
# with open('public_key.pem', 'wb') as f:
#     f.write(public_pem)