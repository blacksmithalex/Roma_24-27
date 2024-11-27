from math import sqrt
def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def isprime_boosted(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def dividers(n):
    gg = []
    for i in range(2, n):
        if n % i == 0:
           gg.append(i)
    return gg

def dividers_boosted(n):
    gg = set()
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            gg.add(i)
            gg.add(n // i)
    return sorted(gg)

condidates = []

for u in range(264871, 322989 + 1):
    gg = []
    ch = dividers_boosted(u)
    if len(ch) == 2 and isprime_boosted(ch[0]) and isprime_boosted(ch[1]) and ch[0] % 10 == ch[1] % 10:
        condidates.append(u)

print(len(condidates), sum(condidates) / len(condidates))