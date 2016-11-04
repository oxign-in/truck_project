from django.db import models
from apps.users.models import User
class Materials(models.Model):
	name = models.CharField(max_length=200)
	created_on = models.DateTimeField(auto_now_add=True)
	delivery_date = models.DateTimeField(blank=True, null=True)
	weight = models.PositiveIntegerField(default = 0)
	source = models.CharField(max_length=200)
	destination = models.CharField(max_length=200)
	created_by = models.ForeignKey(User, related_name='materials')