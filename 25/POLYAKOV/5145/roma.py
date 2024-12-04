def dividers(n):
    gg = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            gg.add(i)
            gg.add(n//i)
    return sorted(gg)
def chet(div):
    count = 0
    for i in div:
        if i % 2 == 0:
            count += 1
    return count

condidates = []
ss = 0
for k in range(0,200000):
    k = 75000000 + k
    gp = dividers(k)
    f = chet(gp)
    if f % 2 != 0:
        print(k - 75000000, f)