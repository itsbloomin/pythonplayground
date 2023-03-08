# web scraping
# https://www.youtube.com/watch?v=XVv6mJpFOb0
from bs4 import BeautifulSoup
import requests

# RB_url = "https://keeptradecut.com/dynasty-rankings/rb-rankings"
    # id: "rankings-page-rankings"
    # class: "class="onePlayer"

#with open(url, 'r') as html_file:
#    content = html_file.read()
#    soup = BeautifulSoup(content, 'html5lib')
#    tags = soup.find_all('li', class_="listitem")
#
#    for tag in tags:
#        print(tag.text.strip())

    # By Class: soup.find_all("div", class_="card-content")
    # By ID:    soup.find(id="ResultsContainer")
    # python_jobs = results.find_all("h2", string="Python")


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html5lib")

results = soup.find(id="ResultsContainer")
jobs = results.find_all("div", class_="card-content")
for job in jobs:
    title = job.find("h2", class_="title")
    company = job.find("h3", class_="company")
    location = job.find("p", class_="location")
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()
