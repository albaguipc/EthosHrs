import http.server
import socketserver
import webbrowser
import os

PORT = 8000
WEB_DIR = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Servidor ejecutándose en http://localhost:{PORT}")
        print("Presiona Ctrl+C para detener el servidor")
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nDeteniendo el servidor...")

if __name__ == "__main__":
    run_server()