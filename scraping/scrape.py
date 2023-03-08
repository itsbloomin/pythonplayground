# web scraping
from bs4 import BeautifulSoup
import html5lib

# url = "https://keeptradecut.com/dynasty-rankings/rb-rankings"
    # id: "rankings-page-rankings"
    # class: "class="onePlayer"

url = "helloworld.html"
with open(url, 'r') as html_file:
    content = html_file.read()
    print(content)