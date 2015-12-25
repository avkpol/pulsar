import os
import sys
sys.path = ['var/www/pulsarvoip'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'pulsarvoip.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


