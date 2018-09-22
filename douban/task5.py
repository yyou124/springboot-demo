import csv
movieslist =[
            "111111111111111",
            "茶馆,9.4,中国大陆,剧情",
            "背靠背，脸对脸,9.4,中国大陆,剧情",
            "鬼子来了,9.2,中国大陆,剧情",
            "哀乐中年,9.2,中国大陆,剧情",]
title =["name,range,location"]
with open('test.csv', 'w', newline='') as moviefile:
    writer = csv.writer(moviefile,delimiter='\t')
    writer.writerow(title)
    for line in movieslist:
        writer.writerow([line]) # to list type

