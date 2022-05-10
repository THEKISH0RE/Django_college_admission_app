import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '2022_StudentsDB',
        'USER':'postgres',
        'PASSWORD': '7010028358',
        'HOST': 'localhost',
        'PORT': '5432'

    }
}