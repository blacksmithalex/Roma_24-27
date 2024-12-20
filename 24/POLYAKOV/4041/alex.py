file = open('24-164.txt')
a = file.read().split()
maxx = 0
for line in a:
    if line.count('G') < 15:
        for letter in set(line):
            maxx = max(maxx, line.rfind(letter) - line.find(letter))
print(maxx)