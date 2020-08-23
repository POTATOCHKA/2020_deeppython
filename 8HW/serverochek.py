import socket
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from nltk.corpus import stopwords
import collections
import json
import threading
import multiprocessing
import logging
import re
from nltk.stem import WordNetLemmatizer


class Server:

    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(('', 9090))
        self.flag = True
        self.quantity = 0

    def work_with_connection(self, conn, addr, q):
        while True:
            try:
                data = conn.recv(1024)
            except:
                break
            if not data:
                break
            data = data.decode('utf-8')
            if data == "SIGUSR1":
                self.flag = False
            temp = [data, conn]
            q.put(temp)
            self.quantity += 1
        conn.close()

    def worker(self, queue, i):
        while True:
            files = queue.get()
            most_common = self.use_url(files[0])
            connect = files[1]
            json_string = json.dumps(most_common)
            connect.send(json_string.encode('utf-8'))

    def use_url(self, data):
        if data == 'SIGUSR!':
            return None
        try:
            response = requests.get(data)  # если ответ успешен, исключения задействованы не будут
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            pass
        else:
            logging.debug('valid request')
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text()
            formatted_str = self.remove_punctuations(text)
            last_list = self.working_text(formatted_str)
            most_common = self.count(last_list)
            return most_common

    def count(self, array_of_words):
        temp = collections.Counter(array_of_words).most_common(10)
        return temp

    def working_text(self, line):
        en_stops = set(stopwords.words('english'))
        ru_stops = set(stopwords.words('russian'))
        other_list = line.split(' ')
        temp = list()
        for i in range(len(other_list)):  # удаление стоп слов eng/rus
            if (other_list[i] in (en_stops or ru_stops)) or (len(other_list[i]) <= 2):
                temp.append(i)
        temp.sort(reverse=True)
        list(map(lambda e: other_list.pop(e), temp))
        lemmatizer = WordNetLemmatizer()  # лемматизация gets->get
        last_list = list(map(lambda w: lemmatizer.lemmatize(w), other_list))
        return last_list

    def remove_punctuations(self, text):
        ntext = re.sub('\W+', ' ', text)  # удаление всех знаков препинания
        new_string = str()
        for i in range(len(ntext)):  # дополнительное форматирование случая kekNumpy->kek Numpy
            if ntext[i].isupper() and (ntext[i - 1] != ' ') and (ntext[i + 1].islower() or ntext[i - 1].islower()):
                new_string += ' '
            new_string += ntext[i]
        other = new_string.lower()  # удаление цифр
        new_text = ''.join(i for i in other if (i.isalpha() or i == ' '))
        return new_text

    def run(self, num):
        list_of_threads = list()
        myqueue = multiprocessing.Queue()
        self.sock.settimeout(0.5)
        for i in range(num):
            proc = multiprocessing.Process(target=self.worker, args=(myqueue, i), daemon=True)
            proc.start()
        self.sock.listen(10)
        while self.flag is True:
            try:
                conn, addr = self.sock.accept()
            except socket.timeout:
                continue
            x = threading.Thread(target=self.work_with_connection, args=(conn, addr, myqueue))
            list_of_threads.append(x)
            x.start()
            if self.flag is False:
                break
        print('server is off, received:', self.quantity - 1, 'urls')


if __name__ == '__main__':
    a = Server()
    print('how many workers u want?')
    n = int(input())
    a.run(n)
