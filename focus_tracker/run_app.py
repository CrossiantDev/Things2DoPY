import http.server
import socketserver
import webbrowser
import os
import sys
import socket

PORT = 5050
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    os.chdir(DIRECTORY)
    local_ip = get_local_ip()
    local_url = f"http://localhost:{PORT}/index.html"
    phone_url = f"http://{local_ip}:{PORT}/index.html"
    
    print("=" * 64)
    print("  ТРЕКЕР ФОКУСА: БВИ + ОЛИМПИАДЫ + ЕГЭ 90+")
    print("=" * 64)
    print(f"  [Компьютер]:  {local_url}")
    print(f"  [Телефон]:    {phone_url}")
    print("-" * 64)
    print("  Инструкция для телефона:")
    print("  1. Подключи телефон к тому же домашнему Wi-Fi.")
    print(f"  2. Открой в браузере телефона адрес: {phone_url}")
    print("  3. Выбери в меню браузера: 'Установить' или 'На экран Домой'.")
    print("-" * 64)
    print("  Для остановки сервера нажмите Ctrl + C")
    print("=" * 64)
    
    webbrowser.open(local_url)
    
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nСервер остановлен.")
            httpd.server_close()

if __name__ == "__main__":
    run()
