file = open('24-264.txt')
a = file.readline()
file.close()

count, countm = 1, 1
for i in range(len(a) - 1):
    rule1 = a[i].isdigit() and a[i + 1].isdigit()
    rule2 = a[i].isalpha() and a[i + 1].isalpha()
    if not(rule1 or rule2):
        count += 1
        if count > countm:
            countm = count
    else:
        count = 1
print(countm)