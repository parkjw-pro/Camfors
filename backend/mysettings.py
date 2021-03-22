DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CFS',
        'USER': 'ssafy304',
        'PASSWORD': 'ssafy304!!',
        'HOST': 'j4a304.p.ssafy.io',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}

SECRET_KEY = '-tnxrx-h#h&ip$^478@2cvdfw#$b$7k(sx5)((-x&8sstj*sg%'
# 