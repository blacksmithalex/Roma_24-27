file = open('24_17878.txt')
a = file.readline()
file.close()
flag_num = False
flag_operator = False
flag_zero = False
count, countm = 0, 0
for x in a:
    if x in '06789':
        if flag_num and not flag_zero:
            count += 1
            countm = max(count, countm)
            flag_num = True
            flag_zero = False
        elif not flag_num and x != '0':
            count += 1
            countm = max(count, countm)
            flag_num = True
            flag_zero = False
        elif flag_operator and x == '0':
            count += 1
            countm = max(count, countm)
            flag_zero = True
            flag_num = True
        else:
            count = 0
            flag_zero = False
        flag_operator = False
    else:
        if not flag_operator and flag_num:
            count += 1
            flag_operator = True
            flag_zero = False
        else:
            count = 0
            flag_operator = False
            flag_zero = False
        flag_num = False
print(countm)