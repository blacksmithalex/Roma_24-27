from math import sqrt


def dividers(n):
    div = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            div.append(i)
            if i != n //i:
                div.append(n // i)
    return div
countm = 0
for i in range(800000, 10**20):
    idiv = dividers(i)
    if len(idiv) != 0:
        pp = (min(idiv) + max(idiv))
        if pp % 10 == 4:
            print(i, pp)
            countm += 1
        if countm == 5:
            break