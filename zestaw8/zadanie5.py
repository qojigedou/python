
n = int(input())

square = []

for i in range(n):
    square.append([])
    ints = input()
    for j in ints.split(" "):
        square[i].append(int(j))

max_rectangle = (0, 0, 0, 0)
max_area = 0
for x in range(n):
    for y in range(n):
        curr = square[x][y]

        for row in range(y, n):
            if square[x][row] != curr:
                break

            for col in range(x, n):
                if square[col][row] != curr:
                    break
                currArea = (col - x + 1) * (row - y + 1)
                if currArea > max_area:
                    max_area = currArea
                    max_rectangle = (x, y, col, row)

print(max_area)
print(max_rectangle)
