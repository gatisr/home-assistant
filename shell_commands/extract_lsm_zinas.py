# python -m pip install requests
import requests
from bs4 import BeautifulSoup
import re

base_url = "https://www.lsm.lv"
html = requests.get(base_url + "/temas/zinas-vieglaja-valoda/").text

soup = BeautifulSoup(html, "html.parser")

# Find the first link element that contains the text "Ziņas vieglajā valodā"
try:
    link = soup.find("a", href=lambda h: h.startswith("/raksts/zinas/zinas-vieglaja-valoda/"))
    # Get the href attribute of the link element
    href = link["href"]

    # Get the html content of the link
    html = requests.get(base_url + href).text
    match = re.search(r'https://static\.lsm\.lv/media/.*?\.mp3', html)
    if match:
        mp3_url = match.group(0)
        print(mp3_url)
    else:
        print("No MP3 URL found")

except TypeError:
    print("No link found")
