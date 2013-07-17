class BaseSecrets(object):
    # Make this unique, and don't share it with anybody.
    SECRET_KEY = 'FILLMEIN'


class DevSecrets(BaseSecrets):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.FILLMEIN',
            'NAME': 'FILLMEIN',
            'USER': 'FILLMEIN',
            'PASSWORD': 'FILLMEIN',
            'HOST': 'FILLMEIN',
            'PORT': 'FILLMEIN',
        }
    }


class ProdSecrets(BaseSecrets):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.FILLMEIN',
            'NAME': 'FILLMEIN',
            'USER': 'FILLMEIN',
            'PASSWORD': 'FILLMEIN',
            'HOST': 'FILLMEIN',
            'PORT': 'FILLMEIN',
        }
    }

