from django.http import HttpResponse
from datetime import datetime
import pytz


DATETIME_TIMEZONE = pytz.timezone('Europe/Moscow')
DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"

def datetime_view(request):
	current_moscow_datetime = datetime.now(DATETIME_TIMEZONE)
	return HttpResponse(current_moscow_datetime.strftime(DATETIME_FORMAT))
