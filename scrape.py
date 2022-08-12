import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())
# for link in soup.find_all('a'):
# print(link.get('href'))
# 'https://news.ycombinator.com/news'

links = soup.select('.storylink')
votes = soup.select('.score')


def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        hn.append(title)
    return hn


print(create_custom_hn(links, votes))
