from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangobasic_db',   
        'USER' : 'root',            
        'PASSWORD' : 'qwer1234',    
        'HOST' : '127.0.0.1',
        'OPTIONS' : {},
    }
}
