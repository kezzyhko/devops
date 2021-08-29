from http.server import BaseHTTPRequestHandler
from datetime import datetime
from config import CHARSET, DATETIME_TIMEZONE, DATETIME_FORMAT


class DatetimeHTTPRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html; charset=' + CHARSET)
		self.end_headers()

		datetime_to_print = datetime.now(DATETIME_TIMEZONE).strftime(DATETIME_FORMAT)
		self.wfile.write(datetime_to_print.encode(CHARSET))