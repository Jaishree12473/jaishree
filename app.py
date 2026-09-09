from http.server import SimpleHTTPRequestHandler, HTTPServer
import mimetypes
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        clean_path = path.split('?')[0].split('#')[0]
        if clean_path in ('', '/'):
            clean_path = '/index.html'
        full_path = os.path.join(ROOT_DIR, clean_path.lstrip('/'))
        return full_path

def app(environ, start_response):
    path = environ.get('PATH_INFO', '/').lstrip('/')
    if not path:
        path = 'index.html'
    
    file_path = os.path.join(ROOT_DIR, path)
    if os.path.isdir(file_path):
        file_path = os.path.join(file_path, 'index.html')
        
    if os.path.exists(file_path) and os.path.isfile(file_path):
        mime, _ = mimetypes.guess_type(file_path)
        mime = mime or 'application/octet-stream'
        with open(file_path, 'rb') as f:
            data = f.read()
        start_response('200 OK', [
            ('Content-Type', mime),
            ('Content-Length', str(len(data)))
        ])
        return [data]
    else:
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'File not found']

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), handler)
    print("Server running on http://localhost:8000")
    server.serve_forever()
