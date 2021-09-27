from django.http import HttpResponse
from datetime import datetime
import pytz
import os


DATETIME_TIMEZONE = pytz.timezone('Europe/Moscow')
DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"

def datetime_view(request):
	current_moscow_datetime = datetime.now(DATETIME_TIMEZONE)
	time_string = current_moscow_datetime.strftime(DATETIME_FORMAT)
	if not os.path.exists('logs'):
		os.mkdir('logs')
	f = open("logs/access.txt", "a")
	f.write(time_string)
	f.write("\n")
	f.close()
	return HttpResponse(time_string)

def visits(request):
	f = open("logs/access.txt", 'r')
	file_content = f.read().replace("\n", "<br>")
	f.close()
	return HttpResponse(file_content)
