file = open('24-1.txt')
a = file.readline()
file.close()

l, r = 0, 0
count_bad = 0
mlen = 0
while r < len(a):
    if a[r] in 'AEIOY':
        count_bad += 1
    if count_bad <= 5:
        mlen = max(mlen, r - l + 1)
    else:
        while count_bad > 5:
            if a[l] in 'AEIOY':
                count_bad -= 1
            l += 1
    r += 1
print(mlen)