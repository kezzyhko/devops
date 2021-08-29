from http.server import HTTPServer, BaseHTTPRequestHandler
from DatetimeHTTPRequestHandler import DatetimeHTTPRequestHandler
from config import ADDR, PORT


if __name__ == '__main__':
	server = HTTPServer((ADDR, PORT), DatetimeHTTPRequestHandler)
	server.serve_forever()
