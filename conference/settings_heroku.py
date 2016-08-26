from conference.settings import *
import dj_database_url

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
STATIC_ROOT = 'staticfiles'

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL', None)),
}
