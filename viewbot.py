from selenium import webdriver
from random import randrange
import time

url = "YOUTUBE URL"

refresh_time = 10
browser_list = []

b1 = webdriver.Chrome("THE LOCATION OF CHROMEDRIVER")
b2 = webdriver.Chrome("THE LOCATION OF CHROMEDRIVER")
b3 = webdriver.Chrome("THE LOCATION OF CHROMEDRIVER")
b4 = webdriver.Chrome("THE LOCATION OF CHROMEDRIVER")
b5 = webdriver.Chrome("THE LOCATION OF CHROMEDRIVER")

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
    
