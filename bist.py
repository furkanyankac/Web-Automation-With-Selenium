import csv
from selenium import webdriver
import asyncio

import time
URL = 'https://www.morningstar.com/stocks/xnas/'   #quote
csv_array = []

with open('C:/Users/MONSTER/Desktop/memobist/sembol.csv') as file:
        csv_content = csv.reader(file)
        for row in csv_content:
            csv_array.append(row[0])
array_size = len(csv_array)
chrome = webdriver.Chrome("C:/Users/MONSTER/Desktop/chromedriver.exe")

for i in range(1,10):
    try:
        chrome.get(URL+csv_array[i]+"/quote")
        chrome.maximize_window()
        time.sleep(3)
        first_button = chrome.find_element_by_xpath("//*[@id='keyStats']").click()
        time.sleep(3)
        second_button = chrome.find_element_by_xpath("//*[@id='__layout']/div/div[2]/div[3]/main/div[2]/div/div/div[1]/div[1]/div/sal-components/section/div/div/div/sal-components-quote/div/div/div/div/div/div[2]/div[2]/sal-components-key-stats/div/div/div/div/a").click()
        time.sleep(3)
        chrome.switch_to.window(chrome.window_handles[1])
        time.sleep(3)
        third_button = chrome.find_element_by_xpath("//*[@id='financials']/div[2]/div/a").click()
        time.sleep(3)
        chrome.switch_to.window(chrome.window_handles[0])
    except:
        print("Bir hata oluştu.")
        continue
time.sleep(2)

chrome.close()