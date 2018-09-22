import expanddouban


"""
return a string corresponding to the URL of douban movie lists given category and location.
"""


def getMovieUrl(category, location):
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"
    url = url + "," + category + "," + location
    return url


print(getMovieUrl("剧情", "美国"))
