import threading
import time
import socket
import logging
import requests
import queue


def kek(n):
    print('nachalo')
    time.sleep(4)
    print('konec')


def upload_url(que):
    logging.debug("pedik: pognal")
    lock.acquire()
    url = que.get()
    html = requests.get(url)
    print(html.text[0:10])
    lock.release()


if __name__ == '__main__':
    """x = threading.Thread(target=kek, args=(1000,))
    x.setDaemon(True)
    print('do treda')
    x.start()
    x.join()
    print('konecprogi')"""
    """ for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()"""
    logging.basicConfig(filename='logs.txt', filemode='w', level=logging.DEBUG)
    sock = socket.socket()
    sock.bind(('127.0.0.1', 9090))
    sock.listen(5)
    client_conn, client_addr = sock.accept()
    logging.debug(f"connected: {client_addr}")
    threads = list()
    lock = threading.Lock()
    q = queue.Queue()
    n_workers = 3
    temp = 0
    for index in range(n_workers):
        x = threading.Thread(target=upload_url, args=(q,))
        threads.append(x)
        x.start()
    while True:
        try:
            data = client_conn.recv(1024)
        except:
            break
        logging.debug(f"give data{data.decode('utf-8')}")
        if not data:
            break
        q.put(data)
        if temp >= n_workers:
            temp = 0
        temp += 1

    client_conn.close()
