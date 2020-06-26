from django.db import models
from django.contrib.auth.models import AbstractUser

MAX_FIELD_LEN = 63

class User(AbstractUser):
	pass

class Book(models.Model):
	user = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "books")
	title = models.CharField(max_length = MAX_FIELD_LEN)
	author = models.CharField(max_length = MAX_FIELD_LEN)
	page = models.IntegerField()
	status = models.IntegerField()
	start_date = models.DateField(auto_now_add = True)
