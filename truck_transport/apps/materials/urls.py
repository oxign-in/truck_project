from django.conf.urls import url

from apps.materials.views import *

urlpatterns = [
    url(r'^$', materials_list, name='materials_list'),
    url(r'^create/$', materials, name='materials_create'),
]