
from bs4 import BeautifulSoup
import requests

url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"

# html = requests.get(url).text
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

content_div = soup.find(id="content").find_all(class_="category")
print(content_div)
# last_a_tag = content_div.find(class_="category")
# print(last_a_tag)
# print(last_a_tag.previous_siblings)
