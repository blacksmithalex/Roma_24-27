file = open('24-25.txt')
a = file.readline()
flag_num = False
flag_alf = False
count = 0
max_cc = 0
for line in a:
    if line in '0123456789':
        count += 1
        if flag_num:
            count = 1
        flag_num = True
        flag_alf = False
        max_cc = max(max_cc, count)
    else:
        count += 1
        if flag_alf:
            count = 1
        flag_alf = True
        flag_num = False
        max_cc = max(max_cc, count)
print(max_cc)