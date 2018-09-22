import requests
from bs4 import BeautifulSoup
"""
description:
http://cn.python-requests.org/zh_CN/latest/
https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
"""
Response = requests.get('https://en.wikipedia.org/wiki/Latin').text

soup = BeautifulSoup(Response, 'html.parser')

first_relative_link = []
content_div = soup.find(id="content").find(class_="mw-parser-output")
for element in content_div.find_all("p", recursive=False):
    if element.find("a", recursive=False):
        first_relative_link.append(element.find("a", recursive=False).get('href'))
        # print(element.a.get('href')
for link in first_relative_link:
    print(link)

def find_first_link(url):
    Response = requests.get(url).text
    soup = BeautifulSoup(Response, 'html.parser')
    # (Sup 15 2018)
    content_div = soup.find(id="content").find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=False):
    if element.find("a", recursive=False):
        link = (element.find("a", recursive=False).get('href'))
        break
    if not link:
        return
    first_link = urllib.pares.urljoin('https://en.wikipedia.org/', link)
    return first_link
