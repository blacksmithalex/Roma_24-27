file = open('24-241.txt')
a = file.readline()
file.close()

glas = 'AEO'
sogl = 'BCDF'
parts = set()
for l1 in glas:
    for l2 in glas:
        for l3 in sogl:
            parts.add(l1 + l2 + l3)
for part in parts:
    a = a.replace(part, '*')

count, countm = 0, 0
for x in a:
    if x == '*':
        count += 1
        if count > countm:
            countm = count
    else:
        count = 0
print(countm)


