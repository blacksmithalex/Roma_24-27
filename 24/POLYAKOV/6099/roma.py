text = open('24-249.txt')
a = text.readline()
digits = '0123456789ABCDEF'
freq = { d: 0 for d in digits }
l, r = 0, 0
candidates = []

while True:
    if 0 in freq.values():
        if r >= len(a): break
        ch = a[r]
        if ch in digits: freq[ch] += 1
        r += 1
    else:
        candidates.append(r - l)
        ch = a[l]
        if ch in digits: freq[ch] -= 1
        l += 1

print(min(candidates))