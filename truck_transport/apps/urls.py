from django.conf.urls import include, url

from apps.materials.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^materials/', include('apps.materials.urls')),
]