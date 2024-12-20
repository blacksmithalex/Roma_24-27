from math import sqrt
def div(n):
    dd = set()
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            dd.add(i)
            dd.add((n//i))
    return sorted(dd)
countm = 0
for i in range(500000, 10**10):
    divi = div(i)
    if len(divi) != 0:
        for j in divi:
            if j != 8 and j % 10 == 8 and i != j:
                print(i, j)
                countm += 1
                break
    if countm == 5:
        break