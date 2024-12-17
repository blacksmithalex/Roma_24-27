countm = 0
num = '6789'
abc = 'ABC'
file = open('24_15339.txt')
a = file.readline()
file.close()
maxx = 0
flagnum, flagabc =  False, False
for line in a:
    if line in abc and flagabc == False:
        flagabc = True
        flagnum = False
        countm += 1
        maxx = max(maxx, countm)
    elif line in num and flagnum == False:
        flagabc = False
        flagnum = True
        countm += 1
        maxx = max(maxx, countm)
    else:
        if line in abc:
            flagnum = False
            countm = 1
        else:
            flagabc = False
            countm = 1
print(maxx)