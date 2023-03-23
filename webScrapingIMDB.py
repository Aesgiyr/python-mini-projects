import requests
from bs4 import BeautifulSoup

url = " https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
result = soup.find("tbody",{"class": "lister-list"}).find_all("tr")

for tr in result:
    title = tr.find('td',{"class":"titleColumn"}).find("a").text
    year = tr.find('td',{"class":"titleColumn"}).find("span").text
    point =tr.find('td',{"class":"ratingColumn"}).find("strong").text
    print(title,year,point+"/10 IMDB Rating")
