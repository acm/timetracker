from django.db import models

class Employee(models.Model):
	name = models.CharField(max_length=100)

class Entry(models.Model):
	employee = models.ForeignKey(Employee)
	project = models.CharField(max_length=100)
	hours	= models.IntegerField()
	description = models.CharField(max_length=200)
	date = models.DateTimeField('date added')
