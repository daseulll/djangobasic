from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',   
        'USER' : 'postgres',            
        'PASSWORD' : 'postgres1234',    
        'HOST' : '127.0.0.1',
        'OPTIONS' : {},
    }
}
