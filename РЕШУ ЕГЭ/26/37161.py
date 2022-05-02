file = open('26.txt')
n, rows = int(file.readline()), {}
for _ in range(n):
    row, seat = [int(x) for x in file.readline().split()]
    rows[row] = rows.get(row, []) + [seat]
file.close()

for row in sorted(rows, reverse=True):
    seats = sorted(rows[row])
    for i in range(len(seats) - 1):
        if seats[i + 1] - seats[i] == 3:
            print(row, seats[i] + 1)
            quit()


