import requests
from bs4 import *

## Парс нужной страницы
def initialization_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

## Заменяет пробелы в ссылке на необходимые знаки 
def change_spaces(string):
    string = string.replace(' ', '%20')
    return string

## Заменяет все заглавние буквы на строчные
def registor(list_names):
    for i in range(len(list_names)):
        list_names[i] = list_names[i].lower()
    return list_names

'''
Названия скинов взяты с сайта wiki.cs.money
weapon_quality - качество оружия
names_of_weapons, links_weapons, low_register_links_weapons - названия оружия
number_of_skins - количество скинов для каждого оружия
'''
weapon_quality = ["Battle-Scarred","Well-Worn", "Field-Tested","Minimal%20Wear", "Factory%20New"]
names_of_weapons = ["AK-47","AWP","M4A4","M4A1-S","AUG","SG%20553","Galil%20AR","FAMAS","SSG%2008","SCAR-20","G3SG1","USP-S","Glock-18","Desert%20Eagle","P250","Five-SeveN","CZ75-Auto","P2000","Tec-9","R8%20Revolver","Dual%20Berettas","P90","UMP-45","MAC-10","MP7","MP9","MP5-SD","PP-Bizon","Sawed-Off","MAG-7","Nova","XM1014","Negev","M249"]
links_weapons = ["AK-47","AWP","M4A4","M4A1-S","AUG","SG-553","Galil-AR","FAMAS","SSG-08","SCAR-20","G3SG1","USP-S","Glock-18","Desert-Eagle","P250","Five-SeveN","CZ75-Auto","P2000","Tec-9","R8-Revolver","Dual-Berettas","P90","UMP-45","MAC-10","MP7","MP9","MP5-SD","PP-Bizon","Sawed-Off","MAG-7","Nova","XM1014","Negev","M249"]
low_register_links_weapons = registor(links_weapons)
number_of_skins = [43 ,37 ,37 ,32 ,36 ,33 ,33 ,32 ,31 ,25 ,28 ,34 ,43 ,35 ,45 ,34 ,32 ,29 ,36 ,19 ,34 ,39 ,35 ,43 ,32 ,32 ,15 ,33 ,31 ,31 ,35 ,33 ,22 ,20]

'''
Проходимся по всем оружиям, берем названия скинов, а также все разновидности с учетом качества
Специальным образом формируем ссылку
'''
with open("Links.txt", "w", encoding="utf-8") as f:
    for z in range(0, 34):
        soup = initialization_page("https://wiki.cs.money/weapons/" + low_register_links_weapons[z])
        data = soup.find_all(class_="zhqwubnajobxbgkzlnptmjmgwn")
        for i in range(0, number_of_skins[z]):
            for j in range(0, 5):
                f.write("https://steamcommunity.com/market/listings/730/" + names_of_weapons[z] + "%20%7C%20" + change_spaces(data[i].get_text()) + "%20%28" + weapon_quality[j] + "%29" + "\n")
