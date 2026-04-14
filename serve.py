#!/usr/bin/env python3
import http.server, socketserver, os

PORT = 4400
DIR = "/Users/zhuya/Documents/GitHub/Biblely/.claude/worktrees/vibrant-heisenberg"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
