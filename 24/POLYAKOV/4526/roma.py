file = open('24-181.txt')
a = file.readline()
file.close()
dd = []
a = a.split(".")
for i in range(3, len(a)):
    dd.append(len(a[i-3]) + len(a[i-2]) + len(a[i - 1]) + len(a[i]) + 3)
print(max(dd))