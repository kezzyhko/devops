from django.test import TestCase
import views
from datetime import datetime, timedelta



class DatetimeViewTest(TestCase):

	def setUp(self):
		self.response = views.datetime_view(None)

	def test_response_code(self):
		self.assertEquals(self.response.status_code, 200)

	def test_format(self):
		try:
			datetime.strptime(self.response.content.decode(), views.DATETIME_FORMAT)
		except ValueError:
			self.fail("Wrong datetime format")

	def test_time_close(self):
		datetime_to_test = datetime.strptime(self.response.content.decode(), views.DATETIME_FORMAT)
		current_datetime = datetime.now()
		diff = abs(datetime_to_test - current_datetime)
		self.assertLess(diff, timedelta(seconds=10))
