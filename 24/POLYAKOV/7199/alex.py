file = open('24-280.txt')
a = file.readline()
file.close()

freq = {}
l = 0
countm = 0
for r in range(len(a)):
    letter = a[r]
    freq[letter] = freq.get(letter, 0) + 1
    if max(freq.values()) <= 10:
        countm = max(countm, r - l + 1)
    else:
        while max(freq.values()) > 10:
            letter = a[l]
            freq[letter] -= 1
            l += 1
print(countm)


