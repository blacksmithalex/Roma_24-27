file = open('26_15341.txt')
b = file.readline()
a = [int(x) for x in file.read().split()]
sortt = sorted(a, reverse= True)
cake = []
tru = None
for i in range(int(b)):
    if tru == None:
        tru = sortt[i]
        cake.append(tru)
    else:
        if tru - sortt[i] >= 8:
            tru = sortt[i]
            cake.append(tru)
print(len(cake), min(cake))
