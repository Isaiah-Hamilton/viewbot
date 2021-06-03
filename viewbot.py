from selenium import webdriver
from random import randrange
import time

url = "YOUTUBE URL"

refresh_time = 10
browser_list = []

chrome = webdriver.Chrome("THE LOCATION OF CHROMEDRIVER")
browser_list.append(chrome)

for browser in browser_list:
    browser.get(url)

while(True):
    browser_num = randrange(0, len(browser_list))
    browser_list[browser_num].refresh()
    print("browser number ", browser_num, "has been refreshed")
    time.sleep(refresh_time)
