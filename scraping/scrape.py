# web scraping
# https://www.youtube.com/watch?v=XVv6mJpFOb0
from bs4 import BeautifulSoup

# url = "https://keeptradecut.com/dynasty-rankings/rb-rankings"
    # id: "rankings-page-rankings"
    # class: "class="onePlayer"

url = "helloworld.html"
with open(url, 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'html5lib')
    tags = soup.find_all('li')

    for tag in tags:
        print(tag)