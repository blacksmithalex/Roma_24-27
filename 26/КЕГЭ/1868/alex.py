file = open('26_1868.txt')
N = int(file.readline())
seats = {} #key(int)-номер ряда / val(list)-занятые места
for _ in range(N):
    row, seat = [int(x) for x in file.readline().split()]
    seats[row] = seats.get(row, []) + [seat]
file.close()

for row in sorted(seats, reverse= True):
    curseats = sorted(seats[row])
    for i in range(len(curseats) - 1):
        if curseats[i + 1] - curseats[i] == 3:
            print(row, curseats[i] + 1)

