
from bs4 import BeautifulSoup
import requests

url = "https://www.10minutemail.com"


def getmail(url):
    r = requests.get(url, timeout=5)

    pc = BeautifulSoup(r.content, "html.parser")

    email = pc.find("input", {"id": "mailAddress"}).get('value')

    print(email)



for x in range(1,20):
    getmail(url)
