import aiohttp
import asyncio
import time
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from collections import Counter
import string
from concurrent.futures import ThreadPoolExecutor
import functools
import requests
import re
from nltk.stem import WordNetLemmatizer
import collections


def count(array_of_words):
    temp = collections.Counter(array_of_words).most_common(10)
    return temp


def working_text(line):
    en_stops = set(stopwords.words('english'))
    ru_stops = set(stopwords.words('russian'))
    other_list = line.split(' ')
    temp = list()
    for i in range(len(other_list)):  # удаление стоп слов eng/rus
        if (other_list[i] in (en_stops or ru_stops)) or (len(other_list[i]) <= 2):
            temp.append(i)
    temp.sort(reverse=True)
    list(map(lambda e: other_list.pop(e), temp))
    return other_list


def remove_punctuations(text):
    ntext = re.sub('\W+', ' ', text)  # удаление всех знаков препинания
    new_string = str()
    for i in range(len(ntext)):  # дополнительное форматирование случая kekNumpy->kek Numpy
        if ntext[i].isupper() and (ntext[i - 1] != ' ') and (ntext[i + 1].islower() or ntext[i - 1].islower()):
            new_string += ' '
        new_string += ntext[i]
    other = new_string.lower()  # удаление цифр
    new_text = ''.join(i for i in other if (i.isalpha() or i == ' '))
    return new_text


def parse(data):
    soup = BeautifulSoup(data, 'html.parser')
    text = soup.get_text()
    formatted_str = remove_punctuations(text)
    last_list = working_text(formatted_str)
    most_common = count(last_list)
    return most_common


async def task(queue, session, i):
    while not queue.empty():
        url = await queue.get()
        pool = ThreadPoolExecutor(max_workers=4)
        loop = asyncio.get_running_loop()
        async with session.get(url) as response:
            data = await response.text()
        result = await loop.run_in_executor(pool, functools.partial(parse, data))
        print(result)


async def main(n):
    queue = asyncio.Queue()
    with open('urls.txt', 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f]
    for url in urls:
        await queue.put(url)
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(n):
            tasks.append(asyncio.create_task(task(queue, session, i)))
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    print('quantity of requests:')
    number = int(input())
    start = time.time()
    asyncio.run(main(number))
    stop = time.time()
    print('Total time: ', stop - start)
