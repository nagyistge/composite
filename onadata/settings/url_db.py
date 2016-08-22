import os

configuration = os.getenv('DJANGO_CONFIGURATION', 'Dev')
if configuration == 'Dev':
    from onadata.settings.staging_example import *  # noqa
else:
    from production_example import *  # noqa

url = os.getenv('DATABASE_URL')

if url:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config(url)}
    # Replacement for TransactionMiddleware
    DATABASES['default']['ATOMIC_REQUESTS'] = True
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
            # Replacement for TransactionMiddleware
            'ATOMIC_REQUESTS': True,
        }
    }

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'xmlfs33xPBHTCR6a36$0#j%dd*sis')
