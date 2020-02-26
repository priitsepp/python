import requests
from bs4 import BeautifulSoup
page = requests.get('https://www.bbc.com/')

soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find(id="page")

kuumimuudis = result.find("a", class_= "media__link")
vastus = kuumimuudis.text

def convert(lst):
    return(lst[0].split())

vastusListSegane =[vastus]
vastusList = convert(vastusListSegane)

parseTester =" "
LoplikLause = ""

for x in vastusList:
    LoplikLause = LoplikLause + " " + x
print(LoplikLause)