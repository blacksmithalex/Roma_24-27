from string import ascii_uppercase
file = open('24-157.txt')
a = file.readline()
b = ascii_uppercase
ff = {d: 0 for d in b}
for i in range(1, len(a) - 1):
    try:
        if a[i] == a[i - 1]:
            ff[a[i + 1]] += 1
    except:
        print(a[i + 1])
print(ff)