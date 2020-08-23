import requests
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import collections

string1 = "https://pythonworld.ru/"
string2 = 'https://python-scripts.com/requests'
string3 = 'https://www.python.org/'
html = requests.get(string3).text
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()  # берем только текст с сайта
# new_text = ''.join(e for e in text if (e.isalnum() or e==' '))
an_new_text = re.sub('\W+', ' ', text)  # удаление всех знаков препинания
new_string = str()
for i in range(len(an_new_text)):  # дополнительное форматирование случая kekNumpy->kek Numpy
    if an_new_text[i].isupper() and (an_new_text[i - 1] != ' ') and (
            an_new_text[i + 1].islower() or an_new_text[i - 1].islower()):
        new_string += ' '
    new_string += an_new_text[i]
other = new_string.lower()  # удаление цифр
new_text = ''.join(i for i in other if (i.isalpha() or i == ' '))
other = new_text
""""""
en_stops = set(stopwords.words('english'))
ru_stops = set(stopwords.words('russian'))
other_list = other.split(' ')
temp = list()
for i in range(len(other_list)):  # удаление стоп слов eng/rus
    if (other_list[i] in (en_stops or ru_stops)) or (len(other_list[i]) <= 2):
        temp.append(i)
temp.sort(reverse=True)
list(map(lambda e: other_list.pop(e), temp))
lemmatizer = WordNetLemmatizer()  # лемматизация gets->get
last_list = list(map(lambda w: lemmatizer.lemmatize(w), other_list))
default_d = collections.defaultdict(int)
for i in last_list:
    default_d[i] += 1
asd = sorted(default_d.items(), key=lambda x: x[1], reverse=True)
wsd = collections.Counter(last_list).most_common(10)
print(wsd,'\n',asd)
