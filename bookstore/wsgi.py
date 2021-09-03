"""
WSGI config for bookstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from dj_static import Cling
#sys.path.append('/home/ubuntu/bookstore/django_bookstore/django_bookstore/src/bookstore')
sys.path.append('/home/ubuntu/bookstore/django_bookstore/django_bookstore/src')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

application = get_wsgi_application()
#application = Cling(get_wsgi_application())
