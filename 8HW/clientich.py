import socket
import json
import time
import threading
import queue


class Client:
    def __init__(self, n_senders, file):
        self.n_senders = n_senders
        self.file = file
        self.q = queue.Queue()

    def send_data(self, file, sock):
        while not self.q.empty():
            url = self.q.get()
            sock.sendall(url.encode('utf-8'))
            raw_data = sock.recv(1024)
            print(raw_data.decode('utf-8'))
            self.q.task_done()
        time.sleep(10)
        sock.close()

    def run(self):
        f = open(self.file, 'r')
        l = [line.strip() for line in f]
        for i in l:
            self.q.put(i)
        sock = socket.socket()
        sock.connect(('127.0.0.1', 9090))
        list_of_threads = list()
        for i in range(self.n_senders):
            x = threading.Thread(target=self.send_data, args=(self.file, sock))
            list_of_threads.append(x)
            x.start()


if __name__ == '__main__':
    print('количество потоков на клиенте:')
    n = int(input())
    a = Client(n, 'urls.txt')
    a.run()
