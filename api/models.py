from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

MAX_FIELD_LEN = 63

class User(AbstractUser):
	pass

STATUS = [
	('0', 'to read'),
	('1', 'reading'),
	('2', 'finished')
]
class Book(models.Model):
	user = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "books")
	title = models.CharField(max_length = MAX_FIELD_LEN)
	author = models.CharField(max_length = MAX_FIELD_LEN)
	page = models.IntegerField()
	status = models.CharField(max_length = 1, choices = STATUS, default = '0')
	start_date = models.DateField(auto_now_add = True)
