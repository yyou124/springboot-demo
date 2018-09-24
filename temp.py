dic = [('中国', 59), ('美国', 53), ('英国', 49)]


fp = open('testtt.txt', 'w+')
for line in dic:
    fp.write(str(line[0]))
    fp.write('\n')  
fp.close()

