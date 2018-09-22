# encodeing -utf-8-
import csv
import operator


def getSting(category, category_list, category_num):
    percentage1 = 100 * category_list[0][1]/category_num
    percentage2 = 100 * category_list[1][1]/category_num
    percentage3 = 100 * category_list[2][1]/category_num
    string = "{}类别中，数量排名前三的地区为{}、{}、{}，分别占此类别电影总数的百分比\
为{:.2f}%、{:.2f}%、{:.2f}%"
    return string.format(category, category_list[0][0], category_list[1][0],
            category_list[2][0], percentage1, percentage2,  percentage3)


with open('C:\CodeLib\Python\movies.csv', 'r') as f:
    reader = csv.reader(f)
    movieslist = list(reader)
categorys = ["剧情", "动作", "动画"]
loc_juqing, loc_dongzuo, loc_donghua = dict(), dict(), dict()
num_juqiang, num_dongzuo, num_donghua = 0, 0, 0
for elments in movieslist:
    if elments[3] == "剧情":
        num_juqiang += 1
        if elments[2] in loc_juqing:
            loc_juqing[elments[2]] += 1
        else:
            loc_juqing[elments[2]] = 1
    if elments[3] == "动作":
        num_dongzuo += 1
        if elments[2] in loc_dongzuo:
            loc_dongzuo[elments[2]] += 1
        else:
            loc_dongzuo[elments[2]] = 1
    if elments[3] == "动画":
        num_donghua += 1
        if elments[2] in loc_donghua:
            loc_donghua[elments[2]] += 1
        else:
            loc_donghua[elments[2]] = 1
loc_juqing = sorted(loc_juqing.items(), key=operator.itemgetter(1), reverse=True)
loc_dongzuo = sorted(loc_dongzuo.items(), key=operator.itemgetter(1), reverse=True)
loc_donghua = sorted(loc_donghua.items(), key=operator.itemgetter(1), reverse=True)

fp = open('testtt.txt', 'w+')
fp.write(getSting(categorys[0], loc_juqing, num_juqiang))
fp.write('\n')
fp.write(getSting(categorys[1], loc_dongzuo, num_dongzuo))
fp.write('\n')
fp.write(getSting(categorys[2], loc_dongzuo, num_donghua))
fp.write('\n')
fp.close()

print(getSting(categorys[0], loc_juqing, num_juqiang))