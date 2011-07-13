"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from models import Entry, Employee
from django.test import TestCase
from mock import patch, patch_object
from StringIO import StringIO

class EntriesTest(TestCase):
	def test_home_shoes_foo_name(self):
		employee = Employee.objects.create(name='Ryan Padget')
		Entry.objects.create(employee=employee, project='HQC', hours=3)
		response = self.client.get('/entries/1/')
		self.assertContains(response, 'HQC')

	#patches sent through url
	@patch('urllib2.urlopen')
	def test_with_mock(self, mock_urlopen):
		mock_response = StringIO('Suivez vos passions')
		mock.return_value = mock_repsonse
		response = self.client.get('/twittertest/')
		self.assertContains(response, 'Already using Twitter via SMS?')

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

