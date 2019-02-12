from django.db import models


# Create your models here.
class Event(models.Model):
	event_name = models.CharField(max_length=100)
	host = models.ForeignKey('user.User', on_delete=models.CASCADE, default=0)
	event_date = models.CharField(max_length=30)
	description = models.CharField(max_length=280)
	location = models.CharField(max_length=50)
	pub_date = models.DateTimeField(auto_now_add=True)
	tags = models.CharField(max_length=100)


	def __str__(self):
		return self.event_name