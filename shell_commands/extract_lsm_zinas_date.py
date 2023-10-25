import requests
from bs4 import BeautifulSoup
import re

base_url = "https://www.lsm.lv"
html = requests.get(base_url + "/temas/zinas-vieglaja-valoda/").text

soup = BeautifulSoup(html, "html.parser")

# Find the first link element that contains the text "Ziņas vieglajā valodā"
try:
    link = soup.find("a", href=lambda h: h.startswith("/raksts/zinas/zinas-vieglaja-valoda/"))
    text = link.text.strip()
    print(text)

except TypeError:
    print("No link found")
