#!/usr/bin/env python3
"""
Servidor local para ver o site.  Uso:  python3 tools/serve.py

Atende pedidos parciais (Range), que é o que o navegador usa para tocar
vídeo — sem isso o vídeo do hero não roda direito no teste local.
"""
import http.server
import os
import re
import socketserver
import webbrowser
from pathlib import Path

PORT = 6040
os.chdir(Path(__file__).resolve().parent.parent)


class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        self.send_header("Accept-Ranges", "bytes")
        super().end_headers()

    def send_head(self):
        rng = self.headers.get("Range")
        if not rng:
            return super().send_head()

        m = re.match(r"bytes=(\d*)-(\d*)$", rng.strip())
        path = self.translate_path(self.path)
        if not m or not os.path.isfile(path):
            return super().send_head()

        size = os.path.getsize(path)
        first, last = m.group(1), m.group(2)
        if first == "":                      # bytes=-500 → os últimos 500
            start, end = max(0, size - int(last or 0)), size - 1
        else:
            start = int(first)
            end = int(last) if last else size - 1
        end = min(end, size - 1)
        if start > end:
            self.send_error(416, "Requested Range Not Satisfiable")
            return None

        f = open(path, "rb")
        f.seek(start)
        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(end - start + 1))
        self.end_headers()
        # o handler envia o arquivo inteiro a partir daqui; recortamos o pedaço
        return _Slice(f, end - start + 1)


class _Slice:
    """Devolve só o pedaço pedido do arquivo e depois acaba."""

    def __init__(self, f, remaining):
        self.f, self.remaining = f, remaining

    def read(self, n=-1):
        if self.remaining <= 0:
            return b""
        n = self.remaining if n is None or n < 0 else min(n, self.remaining)
        data = self.f.read(n)
        self.remaining -= len(data)
        return data

    def close(self):
        self.f.close()


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


with Server(("", PORT), H) as httpd:
    url = f"http://localhost:{PORT}/"
    print(f"La Sirene Tanning rodando em {url}\nCtrl+C para parar.")
    webbrowser.open(url)
    httpd.serve_forever()
