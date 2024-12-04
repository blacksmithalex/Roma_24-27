def dividers(n):
    gg = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            gg.add(i)
            gg.add(n//i)
    return sorted(gg)

condidates = []
ss = 0
for u in range(268220, 270335):
    ch = dividers(u)
    if len(ch) <= 4:
        condidates.append([sum(ch), len(ch)])
print(max(condidates))