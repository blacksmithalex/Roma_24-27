ile = open('24_10105.txt')
a = file.readline()
file.close()
l = 0
r = 0
count = 0
maxx = 0
for r in range(len(a)):
    if a[r] == 'T':
        count += 1
    if count <= 100:
        maxx = max(maxx, r - l + 1)
    else:
        while count > 100 and l < r:
            if a[l] == 'T':
                count -= 1
            l += 1
print(maxx)