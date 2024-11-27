file = open('24-1.txt')
a = file.readline()
ff = {d: 0 for d in 'AEIOUY'}
r, l = 0,0
count = 0
while r < len(a):
    if a[r] in 'AEIOUY':
        ff[a[r]] += 1
    if sum(ff.values()) <= 5:
        count = max(count, r - l + 1)
    else:
        while sum(ff.values()) > 5:
            if a[l] in 'AEIOUY':
                ff[a[l]] -= 1
            l += 1
    r += 1
print(count)