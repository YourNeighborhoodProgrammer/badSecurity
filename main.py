import requests
from bs4 import BeautifulSoup

dosSent = 97764325817654936287547638234872534852874354274527654376257


def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a'):
        print(link.get('href'))


for i in dosSent:
    scrape_website(REPLACE_WITH_TARGET)
    print(i)
print("operation complete")
