from django.forms import ModelForm
from django.db import models

class Employee(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Entry(models.Model):
	employee = models.ForeignKey(Employee)
	project = models.CharField(max_length=100)
	hours	= models.IntegerField()
	description = models.CharField(max_length=200)
	date = models.DateTimeField('date added')

	class Meta:
		verbose_name_plural = 'Entries'

	def __unicode__(self):
		return self.project + ': ' + self.description + ' (' + str(self.hours) + ')'

class EntryForm(ModelForm):
	class Meta:
		model = Entry
