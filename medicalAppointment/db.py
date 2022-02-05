import os
BASE_DIR = os.path.dirname(os.path.dirname(os.abspath(__file__)))

#SQLITE

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#psycopg2

#remember install psycopg2 (pip install psycopg2 binary)

#mysql



    