from django.conf.urls import include, url

from apps.goods.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^goods/', include('apps.goods.urls')),
]