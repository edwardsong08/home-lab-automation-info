"""Serve only the public information page; never expose repository files."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

PAGE = Path(__file__).with_name("index.html").read_bytes()

class Handler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.respond(False)

    def do_GET(self):
        self.respond(True)

    def respond(self, body):
        path = urlsplit(self.path).path
        if path not in ("/", "/privacy", "/terms", "/health"):
            self.send_error(404)
            return
        data = b"ok\n" if path == "/health" else PAGE
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8" if path == "/health" else "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-cache")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        if body:
            self.wfile.write(data)

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
