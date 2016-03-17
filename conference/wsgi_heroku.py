from django.core.wsgi import get_wsgi_application
from dj_static import Cling
import os
from whitenoise.django import DjangoWhiteNoise

# Fix django closing connection to MemCachier after every request (#11331)
from django.core.cache.backends.memcached import BaseMemcachedCache
BaseMemcachedCache.close = lambda self, **kwargs: None

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "conference.settings_heroku")

application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(application)
