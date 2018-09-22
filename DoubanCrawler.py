import expanddouban
from bs4 import BeautifulSoup
import csv
import operator
# import requests


class Movie:
    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link

    def get_data(self):
        return "{},{},{},{},{},{}".format(self.name, self.rate, self.location,\
                self.category, self.info_link, self.cover_link)


def getMovieUrl(category, location):
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"
    url = url + "," + category + "," + location
    return url


def getMovies(category, locations):
    movies = []
    for location in locations:
        html = expanddouban.getHtml(getMovieUrl(category, location), True)
        soup = BeautifulSoup(html, 'html.parser')
        content_movie = soup.find(id='content').find(class_='list-wp').find_all("a", reversed=False)
        for element in content_movie:
            name = element.find(class_='title').string
            rate = element.find(class_='rate').string
            # location = location
            # category = category
            info_link = element.get('href')
            cover_link = element.find('img').get('src')
            movies.append(Movie(name, rate, location, category,
                                info_link, cover_link).get_data())
    return movies


def getSting(category, category_list, category_num):
    percentage1 = 100 * category_list[0][1]/category_num
    percentage2 = 100 * category_list[1][1]/category_num
    percentage3 = 100 * category_list[2][1]/category_num
    string = "{}类别中，数量排名前三的地区为{}、{}、{}，分别占此类别电影总数的百分比\
为{:.2f}%、{:.2f}%、{:.2f}%"
    return string.format(category, category_list[0][0], category_list[1][0],
            category_list[2][0], percentage1, percentage2,  percentage3)


locations = ["中国大陆", "美国", "香港", "香港", "台湾", "日本", "韩国", "英国",
             "法国", "德国", "意大利", "西班牙", "印度", "泰国", "俄罗斯", "伊朗",
             "加拿大", "澳大利亚", "爱尔兰", "瑞典", "巴西", "丹麦"]
categorys = ["剧情", "动作", "动画"]
movieslist = []
for category in categorys:
    movieslist.append(getMovies(category, locations))

title = ["电影名,评分,地区,类型,详情连接,海报连接"]
with open('movies.csv', 'w', newline='') as moviefile:
    writer = csv.writer(moviefile, delimiter='\t')
    writer.writerow(title)
    for movies in movieslist:
        for line in movies:
            # to list type
            writer.writerow([line])

with open('C:\CodeLib\Python\pythonLearn\movies.csv', 'r') as f:
    reader = csv.reader(f)
    movieslist = list(reader)
# get the rank of movies
loc_juqing, loc_dongzuo, loc_donghua = dict(), dict(), dict()
num_juqiang, num_dongzuo, num_donghua = 0, 0, 0
for elments in movieslist:
    if elments[3] == categorys[0]:
        num_juqiang += 1
        if elments[2] in loc_juqing:
            loc_juqing[elments[2]] += 1
        else:
            loc_juqing[elments[2]] = 1
    if elments[3] == categorys[1]:
        num_dongzuo += 1
        if elments[2] in loc_dongzuo:
            loc_dongzuo[elments[2]] += 1
        else:
            loc_dongzuo[elments[2]] = 1
    if elments[3] == categorys[2]:
        num_donghua += 1
        if elments[2] in loc_donghua:
            loc_donghua[elments[2]] += 1
        else:
            loc_donghua[elments[2]] = 1
loc_juqing = sorted(loc_juqing.items(), key=operator.itemgetter(1), reverse=True)
loc_dongzuo = sorted(loc_dongzuo.items(), key=operator.itemgetter(1), reverse=True)
loc_donghua = sorted(loc_donghua.items(), key=operator.itemgetter(1), reverse=True)
# write to txt file
fp = open('output.txt', 'w+')
fp.write(getSting(categorys[0], loc_juqing, num_juqiang))
fp.write('\n')
fp.write(getSting(categorys[1], loc_dongzuo, num_dongzuo))
fp.write('\n')
fp.write(getSting(categorys[2], loc_dongzuo, num_donghua))
fp.write('\n')
fp.close()
