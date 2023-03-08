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
rank = 0

for player in players:
    name_div = player.find("div", class_="player-name")
    name = name_div.find("a").text.strip()
    team = player.find("span", class_="player-team").text.strip()
    rank += 1
    value = int(player.find("div", class_="value").text.strip())
    tier_str = player.find("div", class_="player-info").text.strip()
    tier = int(tier_str[4:])

    player_data = {"rank": rank, "tier": tier, "name": name, "team": team, "value": value}
    running_backs.append(player_data)

for rb in running_backs:
    print(rb)