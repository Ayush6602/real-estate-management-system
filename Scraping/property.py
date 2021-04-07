from selenium import webdriver
import json
import random
import string
import sys

if sys.platform == 'win32':
    driver = webdriver.Chrome('chromedriver_win32\chromedriver.exe')
else:
    driver = webdriver.Chrome('chromedriver_linux64\chromedriver')

with open('dealers.json', 'r') as dealers_file:
    dealers_json = json.load(dealers_file)
    for dealer in dealers_json:
        driver.get(dealer['property_link'])
