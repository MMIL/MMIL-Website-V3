from django.db import models

# Create your models here.
class Student_Registration(models.Model):
	name=models.CharField(max_length=255)
	admission_no=models.CharField(max_length=255)
	interests=models.CharField(max_length=255)
	branch=models.CharField(max_length=255)
	year=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	phone_no=models.IntegerField()

	

	def __str__(self):
		return self.name