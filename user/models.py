from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	gender = models.CharField(max_length=1, default=0)
	bio = models.TextField(max_length=280)
	join_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

