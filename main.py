from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
import csv

name_ = input()
page = 1

options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
while True:
    driver.get(f"https://lis-skins.ru/market/csgo/?query={name_}&page={page}")
    time.sleep(0.5)
    # Получаем html-код страницы
    html = driver.page_source
    
    # Используем BeautifulSoup4 для анализа html-кода
    soup = BeautifulSoup(html, "lxml")

    PRICE_LIST = []
    NAME_LIST = []
    LIST_RESULT = []
    price_element = soup.find_all(class_='price')
    for i in price_element:
        if i:
            price_text = i.get_text(strip=True)
            PRICE_LIST.append(price_text)

    name_inner = soup.find_all(class_='name-inner')
    for i_2 in name_inner:
        NAME_LIST.append(i_2.text)
   
    for name, price in zip(NAME_LIST, PRICE_LIST):
        LIST_RESULT.append({name: price})
    if not PRICE_LIST and not NAME_LIST:
        break
    else:
        page += 1
    with open('ваш_файл.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Записываем каждый элемент списка в отдельной строке
        for item in LIST_RESULT:
            writer.writerow([item])
        
driver.close()
driver.quit()



