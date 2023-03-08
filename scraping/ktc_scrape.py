# Scrape KeepTradeCut Dynasty RB Rankings
from bs4 import BeautifulSoup
import requests

    # id: "rankings-page-rankings"
    # class: "class="onePlayer"

RB_URL = "https://keeptradecut.com/dynasty-rankings/rb-rankings"
page = requests.get(RB_URL)
soup = BeautifulSoup(page.content, "html5lib")

results = soup.find(id="rankings-page-rankings")
players = results.find_all("div", class_="onePlayer")

running_backs = []

for player in players:
    name_div = player.find("div", class_="player-name")
    name = name_div.find("a")
    running_backs.append(name.text.strip())

for back in running_backs:
    print(back)


