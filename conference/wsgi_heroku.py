from django.core.wsgi import get_wsgi_application
from dj_static import Cling
import os
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "conference.settings.heroku")

application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(application)
