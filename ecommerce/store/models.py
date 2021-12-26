from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#customer database model
class Customer(models.Model):
	#one user is binded with one customer
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)

	#return name for admin interface
	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False, null=True, blank=True)

	def __str__(self):
		return self.name