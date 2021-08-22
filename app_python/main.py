from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import pytz



ADDR = ''
PORT = 5000
CHARSET = 'utf-8'
DATETIME_TIMEZONE = pytz.timezone('Europe/Moscow')
DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"



class DatetimeHTTPRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html; charset=' + CHARSET)
		self.end_headers()

		datetime_to_print = datetime.now(DATETIME_TIMEZONE).strftime(DATETIME_FORMAT)
		self.wfile.write(datetime_to_print.encode(CHARSET))
		



if __name__ == '__main__':
	server = HTTPServer((ADDR, PORT), DatetimeHTTPRequestHandler)
	server.serve_forever()