f = open("../input.txt", 'r')
count = 0
first = int(f.readline())
second = int(f.readline())
third = int(f.readline())

previous = first + second + third
first = second
second = third

while True:
    third = f.readline()
    if not third:
        break
    third = int(third)
    current = first + second + third
    if current > previous:
        count += 1
    previous = current
    first = second
    second = third
print(count)