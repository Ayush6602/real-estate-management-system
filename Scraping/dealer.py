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
dealers_dicts = []
mails = ['gmail', 'yahoo', 'outlook', 'iiitg']

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
        username = name.replace(' ', '_').lower()
        password = username
        mail: str = username.replace('_', '.') + ''.join([random.choice(
            string.digits) for _ in range(4)]) + '@' + random.choice(mails) + '.com'
        phone_number: str = ''.join(
            [random.choice(string.digits) for _ in range(10)])
        print(locality, name, property_link, phone_number, mail, sep='\n')
        dealers.append('(' + '"' + username + '"' + ',' + '"' + password + '"' + ',' + '"' + name + '"' + ',' +
                       phone_number + ',' + '"' + mail + '"' + ')')
        dealers_dicts.append({
            'username': username,
            'password': password,
            'name': name,
            'contact_number': phone_number,
            'mail': mail,
            'locality': locality
        })
        i += 1
finally:
    with open('dealers.txt', 'w') as dealers_txt:
        dealers_txt.write(',\n'.join(dealers) + ';')
    with open('dealers.json', 'w') as dealers_json:
        json.dump(dealers_dicts, dealers_json)
    driver.quit()
