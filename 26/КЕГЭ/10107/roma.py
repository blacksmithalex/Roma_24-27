file = open('26_10107.txt')
b = file.readline()
condidates = []
conf = [[int(x) for x in line.split()] for line in file]
conf = sorted(conf, key= lambda x: x[1])
flag = False
end = 0
countm = 1
dlina = 0
pp = max(conf, key= lambda x: x[0])
for i in conf:
    if not flag:
        condidates.append(i)
        end = i[1]
        flag = True

    else:
        if i[0] >= end:
            condidates.append(i)
            end = i[1]
            dlina = max(dlina, i[0] - end)
print(len(condidates), '15')