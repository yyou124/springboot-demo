import time
import requests
import urllib
from bs4 import BeautifulSoup

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"


def continue_crawl(search_history, target_url):
    if target_url in search_history:
        print("We've found the target article!")
        return False
    elif len(search_history) > 25:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    elif search_history[-1] in search_history[:-2]:
        print("We've arrived at an article we've seen, aborting search!")
        return False
    else:
        return True


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
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', link)
    return first_link


article_chain = [start_url]
while continue_crawl(article_chain, target_url):
    # print(len(article_chain)-1)
    print(str(len(article_chain)-1)+": "+article_chain[-1])
    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break
    article_chain.append(first_link)

    time.sleep(3)
