from http.server import HTTPServer, BaseHTTPRequestHandler
from src.controller.StudentDAO import StudentDAO
import json


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/list':
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            self.get_students()
        else:
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write("Students API".encode())

    def get_students(self):
        student = StudentDAO()
        self.wfile.write(json.dumps(student.list_students(0)).encode())


def main():
    PORT = 8080
    server = HTTPServer(('', PORT), Handler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()
