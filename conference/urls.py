"""
    Conference Site URL Configuration
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = [
    url(r'login/', login, name="login"),
    url(r'logout/', logout, name="logout"),
    url(r'^admin/login/', login, name="admin_login"),
    url(r'^admin/logout/$', logout, name="admin_logout"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^tinymce-browser/', include('tinymce_browser.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns(
    '', url(r'', include('feincms.urls')),
)
