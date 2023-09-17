# Задача 1: со статьи ISO4217 стянуть себе таблицу, содержащую аббревиатуры, коды и расшифровки валют

# импорты
from bs4 import BeautifulSoup
import requests
from pprint import pprint
from pandas import DataFrame

# ссылка на сайт
url = 'https://en.wikipedia.org/wiki/ISO_4217'

# запрос страницы
page = requests.get(url).text

# перевод в объект BeautifulSoup
soup = BeautifulSoup(page, 'html.parser')
# print(soup.prettify())

# таблица с аббревиатурами
table = soup.find('table', {'class':'wikitable'})

# проба пера
# сформируем требуемые колонки
# pprint(table.findAll('td')[0::5])
# pprint(table.findAll('td')[1::5])
# pprint(table.findAll('td')[3::5])

# print(soup.title.string)
# print(soup.a)
# # print(soup.find('a'))
# pprint(soup.findAll('a'))

def clean_tagarr(tag_arr):
    clean_arr = []
    for tag in tag_arr:
        if bool(tag.a) is True:
            clean_arr.append(tag.a.string)
        else:
            clean_arr.append(tag.string)

    return clean_arr

# Запишем полученные данные в таблицу
df = DataFrame({
    'Code': clean_tagarr(table.findAll('td')[0::5]),
    'Num': clean_tagarr(table.findAll('td')[1::5]),
    'Currency': clean_tagarr(table.findAll('td')[3::5]),
})

# сохраним в csv формате
df.to_csv('curr_codes.csv', index=False, sep=';')





