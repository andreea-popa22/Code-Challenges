def calc_position():
    f = open("../input.txt", 'r')
    lines = f.readlines()
    depth = 0
    horizontal = 0
    aim = 0
    for line in lines:
        direction, number = line.split()
        if direction == "forward":
            horizontal += int(number)
            depth += int(number)*aim
        elif direction == "down":
            aim += int(number)
        elif direction == "up":
            aim -= int(number)
    return depth * horizontal

print(calc_position())
