import socket
import json


def check_in_url(url):
    if not isinstance(url, str):
        raise TypeError
    if not (url.startswith('https://') or url.startswith('http://')):
        raise TypeError


sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
for i in range(1):
    print('введите ваш url:')
    url = str(input())
    check_in_url(url)
    sock.sendall(url.encode('utf-8'))
    raw_data = sock.recv(1024)
    data = json.loads(raw_data.decode("utf-8"))
    print(data)
sock.close()
