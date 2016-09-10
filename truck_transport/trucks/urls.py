from django.conf.urls import url

from trucks.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
]