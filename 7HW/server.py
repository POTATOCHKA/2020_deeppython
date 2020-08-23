import socket
import logging
import requests
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import collections
import json
from requests.exceptions import HTTPError


class Server:
    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(('', 9090))

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

    def count(self, array_of_words):
        temp = collections.Counter(array_of_words).most_common(10)
        return temp

    def HTTPrequests(self, data):
        try:
            response = requests.get(data)  # если ответ успешен, исключения задействованы не будут
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            logging.debug('valid request')
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text()
            formatted_str = self.remove_punctuations(text)
            last_list = self.working_text(formatted_str)
            most_common = self.count(last_list)
            return most_common

    def go(self, num):
        logging.basicConfig(filename='logs.txt', filemode='w', level=logging.DEBUG)
        sock = socket.socket()
        sock.bind(('127.0.0.1', 9090))
        sock.listen(num)
        while True:
            client_conn, client_addr = sock.accept()
            logging.debug(f"connected: {client_addr}")
            while True:
                try:
                    data = client_conn.recv(1024)
                except:
                    break
                logging.debug(f"{data.decode('utf-8')}")
                if not data:
                    break
                most_common = self.HTTPrequests(data)
                json_string = json.dumps(most_common)
                client_conn.send(json_string.encode('utf-8'))
            client_conn.close()


if __name__ == '__main__':
    a = Server()
    a.go(2)
