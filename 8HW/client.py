import socket
import json
import time

sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
for i in range(1):
    url = 'SIGUSR1'
    sock.sendall(url.encode('utf-8'))
    time.sleep(0.5)
    raw_data = sock.recv(1024)
    print(raw_data.decode('utf-8'))
sock.close()
