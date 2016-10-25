from django.conf.urls import url

from apps.goods.views import *

urlpatterns = [
    url(r'^$', goods_list, name='goods_list'),
    url(r'^create/$', goods, name='goods_create'),
]