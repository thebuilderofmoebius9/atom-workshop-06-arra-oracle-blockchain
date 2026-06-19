#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parent.parent / 'frontend'
RPC = 'http://127.0.0.1:18545'

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'content-type')
        self.send_header('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_POST(self):
        if self.path != '/rpc':
            self.send_error(404)
            return
        length = int(self.headers.get('content-length') or '0')
        body = self.rfile.read(length)
        req = urllib.request.Request(RPC, data=body, headers={'content-type': 'application/json'}, method='POST')
        try:
            with urllib.request.urlopen(req, timeout=10) as r:
                data = r.read()
                self.send_response(r.status)
                self.send_header('content-type', 'application/json')
                self.end_headers()
                self.wfile.write(data)
        except Exception as exc:
            payload = (str(exc) + '\n').encode()
            self.send_response(502)
            self.send_header('content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(payload)

if __name__ == '__main__':
    ThreadingHTTPServer(('0.0.0.0', 8719), Handler).serve_forever()
