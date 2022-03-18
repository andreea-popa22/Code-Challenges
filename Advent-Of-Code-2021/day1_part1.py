f = open("../input.txt", 'r')
count = 0
previous = int(f.readline())

while True:
    current = f.readline()
    if not current:
        break
    current = int(current)
    if current > previous:
        count += 1
    previous = current

print(count)