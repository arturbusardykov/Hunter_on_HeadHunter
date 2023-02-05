import fake_useragent
from requests import Session
from  bs4 import BeautifulSoup
import requests
from time import sleep
from fake_useragent import UserAgent

import selenium as webdriver



headers = { "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.10 Safari/532.0"}


work = Session()


wor, heak.get("https://hh.ru/account/login?backurl=%2F&hhtmFrom=account_login"ders=headers)

response = work.get("https://hh.ru/account/login?backurl=%2F&hhtmFrom=account_login", headers=headers)


soup = BeautifulSoup(response.text,"lxml")

token = soup.find("input",attrs={"name":"_xsrf"}).get("value")

print(token)

data={"_xsrf": token,
"backUrl": "https://hh.ru/",

"failUrl": "/account/login?backurl=%2F",

"accountType": "APPLICANT",

"remember": "yes",
"username": "79057649481",
"password": "Arturb15",
"username": "79057649481",
"isBot": "false"}

result = work.post("https://hh.ru/account/login?backurl=/", headers=headers, data=data, allow_redirects=True)
print(result.text)

# button = driver.find_element(By.CLASS_NAME, 'bloko-button bloko-button_kind-primary bloko-button_stretched')
# button.click()









