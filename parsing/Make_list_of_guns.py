from bs4 import *
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

useragent = UserAgent()
options = webdriver.ChromeOptions()


def options_browser():
    options.add_argument(f"user-agent={useragent.random}")
    options.add_argument('--disable-blink-features=AutomationControlled')


def delete_USD(string):
    string = string.replace(" USD", "")
    string = string.replace("$","")
    string = string.replace(",", ".")
    return string
    

with open("test.txt", "r", encoding="utf-8") as f:
    while True:
        url = f.readline().strip()
        if url == '':
            break
        with open(r"Result\Table\Gun_Info.csv", "a", encoding="utf-8") as a:
            writer = csv.writer(a)
            options_browser()
            driver = webdriver.Chrome(executable_path="C:\\Users\\timof\\Desktop\\Python\\Skin_bot\\chromedriver\\chromedriver.exe", options = options)
            driver.get(url)
            driver.execute_script("g_oSearchResults.GoToPage(1)")
            time.sleep(1)
            driver.execute_script("g_oSearchResults.GoToPage(0)")
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            name = soup.find(class_ = "market_listing_item_name economy_item_hoverable")
            first_price = soup.find(class_="market_listing_price market_listing_price_with_fee")
            writer.writerow([name.text,delete_USD(first_price.text.strip())])
            driver.quit()