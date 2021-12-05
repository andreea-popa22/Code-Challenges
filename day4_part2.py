f = open("../input.txt", 'r')
numbers = f.readline()
numbers = [int(nr) for nr in numbers.split(",")]
boards = []
f.readline()
lines = f.readlines()
last_board = []
winning_board = []
last_number = -1
for line in lines:
    line = line.strip()
    if line:
        last_board.append([int(nr) for nr in line.split()])
    else:
        boards.append(last_board)
        last_board = []

marked = [[[0
           for _3 in range(5)]
          for _2 in range(5)]
          for _1 in range(100)]


def mark_in_board(nr, b, mark):
    for i in range(5):
        for j in range(5):
            if b[i][j] == nr:
                mark[i][j] = 1
                return mark
    return mark


def check_bingo(mark):
    for row in mark:
        if sum(row) == 5:
            return True
    columns = list(zip(*mark))
    for column in columns:
        if sum(column) == 5:
            return True
    return False

score = 0
# Draw numbers
for number in numbers:
    index = 0
    # Check each board for bingo
    while index < len(boards):
        marked[index] = mark_in_board(number, boards[index], marked[index])
        if check_bingo(marked[index]):
            if len(boards) == 1:
                for index1, line in enumerate(boards[index]):
                    for index2, x in enumerate(line):
                        print(x)
                        if marked[index][index1][index2] == 0:
                            score += x
                score *= number
            else:
                boards.remove(boards[index])
                marked.remove(marked[index])
                index -= 1
        index += 1
    if len(boards) == 1:
        break

print("Score: " + str(score))
