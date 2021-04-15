from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=120)
	descritpion = models.TextField()

# title is the reference to the post model in admin 
	def __str__ (self):
		return self.title