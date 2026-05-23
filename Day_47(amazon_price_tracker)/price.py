import requests
from bs4 import BeautifulSoup

url = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
element = soup.find(class_="a-price-whole")
element = element.text+soup.find(class_="a-price-fraction").text

price_as_floating=float(element)

print(price_as_floating)