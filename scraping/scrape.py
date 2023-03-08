# web scraping
# https://www.youtube.com/watch?v=XVv6mJpFOb0
from bs4 import BeautifulSoup
import requests

# Example 1: Local File (no url request)
#with open(url, 'r') as html_file:
#    content = html_file.read()
#    soup = BeautifulSoup(content, 'html5lib')
#    tags = soup.find_all('li', class_="listitem")
#
#    for tag in tags:
#        print(tag.text.strip())

# Example 2: parse job data URL, extract title. company, location
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html5lib")
results = soup.find(id="ResultsContainer")
jobs = results.find_all("div", class_="card-content")
for job in jobs:
    title = job.find("h2", class_="title")
    company = job.find("h3", class_="company")
    location = job.find("p", class_="location")
    print(f"{title.text.strip()}  {company.text.strip()}  {location.text.strip()}")

# Example 3: parse results for jobs containing Python, access parent href elements
print("\n" + "Example 3:" + "\n")
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())

    # list comprehension example: https://realpython.com/list-comprehension-python/
python_job_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]

for job_element in python_job_elements:
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")