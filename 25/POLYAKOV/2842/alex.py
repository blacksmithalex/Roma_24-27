def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a = 12_034_679
b = 23_175_821
for p in range(2, 100):
    if isprime(p):
        num = p**4
        if a <= num <= b:
            print(num, p**3)
