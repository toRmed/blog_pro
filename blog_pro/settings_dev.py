from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGGING = {
    'version':1, # stack 1
    'disable_existing_loggers':False,

    'loggers':{
        'django':{ # logger for django
            'handlers':['console'],
            'level':'INFO',
        },
        'blog_app':{ # logger for application
            'handlers':['console'],
            'level':'DEBUG',
        },
    },
    'handlers':{ # setting for handler
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },
    'formatters':{ # setting for formatter
        'dev':{ 
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'