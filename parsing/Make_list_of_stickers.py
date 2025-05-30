import requests
from bs4 import *
from selenium import webdriver
from fake_useragent import UserAgent
import csv
import time
import random

## Парс нужной страницы
def initialization_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

def options_browser():
    options.add_argument(f"user-agent={useragent.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--headless')

def delete_USD(string):
    string = string.replace(" USD", "")
    string = string.replace("$","")
    string = string.replace(",", ".")
    return string

useragent = UserAgent()
options = webdriver.ChromeOptions()
options_browser()
driver = webdriver.Chrome(executable_path="C:\\Users\\timof\\Desktop\\Python\\Skin_bot\\chromedriver\\chromedriver.exe", options = options)

with open(r"Result\Table\list_of_stickers.csv", 'a', encoding="utf-8") as f:
    writer = csv.writer(f)
    for i in range(1, 122):
        if i % 100 == 0:
            driver.quit()
            options_browser()
            driver = webdriver.Chrome(executable_path="C:\\Users\\timof\\Desktop\\Python\\Skin_bot\\chromedriver\\chromedriver.exe", options = options)
        time.sleep(random.uniform(0.25,0.5))
        driver.get("https://steamcommunity.com/market/search?appid=730&q=%D0%BD%D0%B0%D0%BA%D0%BB%D0%B5%D0%B9%D0%BA%D0%B0#p" + str(i) + "_price_desc")
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        names = soup.find_all(class_="market_listing_item_name_block")
        time.sleep(2)
        prices = soup.find_all(class_="market_listing_right_cell market_listing_their_price")
        print(i)
        for j in range(0, 10):
            name_of_skin = names[j].text.replace("Counter-Strike: Global Offensive", "").strip()
            prices_of_skin = prices[j].text.split("\n")[3]
            result = [name_of_skin, delete_USD(prices_of_skin)]
            writer.writerow(result)
    
