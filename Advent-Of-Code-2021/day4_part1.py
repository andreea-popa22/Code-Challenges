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


def check_bingo(mark):
    for i, row in enumerate(mark):
        if sum(row) == 5:
            return True
    columns = list(zip(*mark))
    for column in columns:
        if sum(column) == 5:
            return True
    return False


# Draw numbers
for number in numbers:
    # Check each board for bingo
    for index, board in enumerate(boards):
        marked[index] = mark_in_board(number, board, marked[index]).copy()
        if check_bingo(marked[index]):
            last_number = number
            winning_board = board
            break
    if winning_board:
        print("Winning_board: " + str(winning_board))
        break

# Calculate score
score = 0
position = boards.index(winning_board)
for index1, line in enumerate(winning_board):
    for index2, number in enumerate(line):
        if marked[position][index1][index2] == 0:
            score += number

score *= last_number
print("Score: " + str(score))
