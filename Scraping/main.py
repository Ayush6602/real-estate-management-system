from selenium import webdriver
import json
import random
import string
import sys

if sys.platform == 'win32':
    driver = webdriver.Chrome('chromedriver_win32\chromedriver.exe')
else:
    driver = webdriver.Chrome('chromedriver_linux64\chromedriver')

print('get: https://www.99acres.com/real-estate-agents-in-guwahati-ffid')
driver.get('https://www.99acres.com/real-estate-agents-in-guwahati-ffid')

dealers = []

try:
    i = 2
    while True:
        locality: str = driver.find_element_by_xpath(
            f'//*[@id = "results"]/div/div[{i}]/div/table/tbody/tr[2]/td/div/div[2]').find_elements_by_tag_name('span')[-1].text
        property_link: str = driver.find_element_by_xpath(
            f'//*[@id="results"]/div/div[{i}]/div/table/tbody/tr[2]/td/div/div[2]/a').get_attribute('href')
        name: str = driver.find_element_by_xpath(
            f'//*[@id="results"]/div/div[{i}]/div/table/tbody/tr[2]/td/div/div[5]').text
        name = name[(name.find(':') + 1):name.find('|')]
        name = name.strip()
        phone_number: str = ''.join(
            [random.choice(string.digits) for _ in range(10)])
        print(locality, name, property_link, phone_number, sep='\n')
        dealers.append({
            'name': name,
            'locality': locality,
            'property_link': property_link,
            'phone_number': phone_number,
        })
        i += 1
finally:
    with open('dealers.json', 'w') as dealers_json:
        json.dump(dealers, dealers_json, indent=4)
    driver.quit()
