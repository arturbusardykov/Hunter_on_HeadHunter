from requests import Session
from  bs4 import BeautifulSoup
import requests
from time import sleep

headers = {"User-Agent": "CroockedHands/2.0 (EVM x8), CurlyFingers20/1;p"}








work = Session()


work.get("https://hh.ru/account/login?backurl=%2F&hhtmFrom=account_login", headers=headers)

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
"password": "Arturb1",
"username": "79057649481",
"isBot": ""}

result = work.post("https://hh.ru/account/login?backurl=/", headers=headers, data=data, allow_redirects=True)
print(result.text)





