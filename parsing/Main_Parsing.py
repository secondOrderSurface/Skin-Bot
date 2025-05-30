import requests
from bs4 import *
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import random

## Обход ограничения сервера на количество запросов
useragent = UserAgent()
options = webdriver.ChromeOptions()


def options_browser():
    options.add_argument(f"user-agent={useragent.random}")
    options.add_argument('--disable-blink-features=AutomationControlled')
    #options.add_argument('--headless')


## Функция возвращающая количество вкладок на одной странице 
def number_of_pages(soup):
    number_of_pages = soup.find(class_="market_paging_controls")
    return number_of_pages.text.split(" ")[-2]


## Парс нужной страницы
def initialization_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup
 
 
## Поиск скина с определенной наклейкой   
def find_skin(parametr):
    search_box = driver.find_element(By.ID, 'market_listing_filter_search_box')
    search_button = driver.find_element(By.ID, 'market_listing_filter_submit')
    search_box.send_keys(parametr)
    search_button.click()


def delete_USD(string):
    string = string.replace(" USD", "")
    string = string.replace("$","")
    string = string.replace(",", ".")
    return string

    
def resist_block(driver):
    driver.get(url)
    check_soup = BeautifulSoup(driver.page_source, 'html.parser')
    cheacker = check_soup.find(id="message")
    if (str(cheacker).split("\n")[0]  == '<div id="message">'): ##
        print("Слишком много запрсов. Возьмём маленький перерыв...")
        time.sleep(240)
        driver.refresh()
            

def check_fact_of_sale(driver):
    check_soup = BeautifulSoup(driver.page_source, 'html.parser')
    cheacker = check_soup.find(class_="market_listing_table_message")
    del check_soup
    if (str(cheacker).split("\n")[0]  == '<div class="market_listing_table_message">'): ## Этот скин никто не продает
        print("Скинь никто не продают")
        return False
    return True
    
    
    


## Передача ссылок на все предметы 
with open(r"Result\Table\test.txt", "r", encoding="utf-8") as f:
    while True:
        url = f.readline().strip()
        if url == '':
            break
        options_browser()
        driver = webdriver.Chrome(executable_path="C:\\Users\\timof\\Desktop\\Python\\Skin_bot\\chromedriver\\chromedriver.exe", options = options)
        driver.get(url)
        print("Создание драйвера")
        time.sleep(1)
        if (check_fact_of_sale(driver) == False): ## Этот скин никто не продает
            continue
        print("Скин продают")
        find_skin("наклейка")
        number_soup = BeautifulSoup(driver.page_source, 'html.parser')
        number_of_pages_ = int(number_of_pages(number_soup))
        del number_soup
        driver.execute_script("g_oSearchResults.GoToPage(1)")
        time.sleep(3)
        driver.execute_script("g_oSearchResults.GoToPage(0)")
        time.sleep(3)
        print("Начало парса скина")
        with open(r"Result\Table\test.csv", "w", encoding="utf-8") as a:
            writer = csv.writer(a)
            for i in range(number_of_pages_):
                resist_block(driver)
                driver.execute_script("g_oSearchResults.GoToPage(" + str(i) + ")")
                print("Переход на новую страницу c номером " + str(i+1))
                time.sleep(5)
                photo = driver.find_elements(By.CLASS_NAME, "market_listing_item_img_container")
                time.sleep(5)                        
                for j in range(len(photo)-1):
                    photo[j].click()  
                    time.sleep(random.uniform(2.2,2.7))
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    stickers = soup.find_all(id="sticker_info")
                    time.sleep(random.uniform(2.7,3.1))
                    prices = soup.find_all(class_="market_listing_price market_listing_price_with_fee")
                    time.sleep(0.5)
                    names = soup.find(class_ = "market_listing_item_name economy_item_hoverable")
                    writer.writerow([names.text, stickers[1].text, delete_USD(prices[j].text.strip())])
                    print("Парс лота номер " + str(j+1))
    print("Конец парса этого скина")
    driver.quit()
                                                        
                        
                
    
        
        
        
        
            
            


    

        