from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
text = 'SECRET_KEY = \'{0}\''.format(secret_key)

with open('./local_settings.py', 'w') as f:
    print(text, file=f)
    print('DEBUG = False', file=f)