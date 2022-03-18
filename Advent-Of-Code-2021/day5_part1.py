f = open("../input.txt", 'r')
lines = f.readlines()

diagram = [[0 for _2 in range(1000)] for _1 in range(1000)]

for line in lines:
    line = line.strip()
    points = line.split(" -> ")
    x1, y1 = map(int, points[0].split(","))
    x2, y2 = map(int, points[1].split(","))
    if x1 == x2:
        for j in range(min(y1, y2), max(y1, y2) + 1):
            diagram[x1][j] += 1
    if y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            diagram[i][y1] += 1

number = 0
for line in diagram:
    number += len(list(filter(lambda x: x > 1, line)))
print(number)
