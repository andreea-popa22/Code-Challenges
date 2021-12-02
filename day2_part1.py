def calc_position():
    f = open("../input.txt", 'r')
    lines = f.readlines()
    depth = 0
    horizontal = 0
    for line in lines:
        direction, number = line.split()
        if direction == "forward":
            horizontal += int(number)
        elif direction == "down":
            depth += int(number)
        elif direction == "up":
            depth -= int(number)
    return depth * horizontal

print(calc_position())
