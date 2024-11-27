def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def dividers(n):
    gg = []
    for i in range(2, n):
        if n % i == 0:
           gg.append(i)
    return gg


for u in range(113012, 113061 + 1):
    ch = dividers(u)
    if len(ch) == 2:
        print(ch[1], u)