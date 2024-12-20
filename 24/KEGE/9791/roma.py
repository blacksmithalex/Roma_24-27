file = open('24_9791.txt')
ff = '123456789ABCDEF'
a = file.readline()
countm = 0
maxx = 0
for line in a:
    if line in ff:
        countm += 1
        maxx = max(maxx, countm)
    else:
        countm = 0
print(maxx)