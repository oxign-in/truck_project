from django.conf.urls import include, url
from users.views import *

urlpatterns = [
	url(r'^register/', register, name='register'),
]
