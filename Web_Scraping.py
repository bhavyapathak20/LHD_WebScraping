import requests
from bs4 import BeautifulSoup

req = requests.get("https://bhavyapathak20.github.io/My-Site/")

soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())

