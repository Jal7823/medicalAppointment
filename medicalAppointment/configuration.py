from pathlib import Path
import os
import os.path



# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-0k-)io5ggcv0%-^up8r$#+yr(z4q1z^$69hna%s-zo9)c5_)r9'

LOCAL_DEBUG = True
WEB_DEBUG = False

WEB_HOSTS = ['medicalAppointment.pythonanywhere.com']
LOCAL_HOSTS = ['*']