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

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'medicalAppointme$medicalService',
        'USER': 'medicalAppointme',
        'PASSWORD': '23051988joswelj',
        'HOST': 'medicalAppointment.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        'STORAGE_ENGINE': 'MyISAM / INNODB / ETC'
    }
}

    