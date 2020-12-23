from selenium import webdriver
from random import randrange
import time

url = ""

refresh_time = 10
browser_list = []


#there is 5 browsers
b1 = webdriver.Chrome("C:\\Users\\Itsis\\chromedriver")
b2 = webdriver.Chrome("C:\\Users\\Itsis\\chromedriver")
b3 = webdriver.Chrome("C:\\Users\\Itsis\\chromedriver")
b4 = webdriver.Chrome("C:\\Users\\Itsis\\chromedriver")
b5 = webdriver.Chrome("C:\\Users\\Itsis\\chromedriver")

#there is 5 text
browser_list.append(b1)
browser_list.append(b2)
browser_list.append(b3)
browser_list.append(b4)
browser_list.append(b5)

for browser in browser_list:
    browser.get(url)

while(True):
    browser_num = randrange(0, len(browser_list))
    browser_list[browser_num].refresh()
    print("browser number ", browser_num, "has been refreshed")
    time.sleep(refresh_time)