import requests
from bs4 import *

## Парс нужной страницы
def initialization_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

## Заменяет пробелы в ссылке на необходимые знаки 
def change_spaces(string):
    string = string.replace('skins', ' ')
    return string

## Парсим названия оружий c сайта wiki.cs.money
with open("number_of_skins.txt", "w", encoding="utf-8") as f:
    soup = initialization_page("https://wiki.cs.money")
    data = soup.find_all(class_="rjloyoqixzsptxrjochnttkdgz")
    for i in range(19, 53):
        f.write(change_spaces(data[i].get_text()) + ",")
        