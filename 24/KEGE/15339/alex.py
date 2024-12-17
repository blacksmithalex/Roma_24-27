file = open('24_15339.txt')
a = file.readline()
file.close()

count, countm = 1, 1
for i in range(len(a) - 1):
    rule1 = a[i].isdigit() and a[i + 1].isalpha()
    rule2 = a[i].isalpha() and a[i + 1].isdigit()
    if rule1 or rule2:
        count += 1
        countm = max(count, countm)
    else:
        count = 1
print(countm)