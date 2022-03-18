f = open("../input.txt", 'r')
lines = f.readlines()
bits = [""]*12
for line in lines:
    for index in range(len(line)-1):   # ignore the newline
        bits[index] += line[index]


def boolString(bool_var):
    if bool_var:
        return "1"
    else:
        return "0"


gamma_rate = ""
epsilon_rate = ""
for index in range(len(bits)):
    gamma_rate += boolString(bits[index].count('1') >= len(bits[index])/2)
    epsilon_rate += boolString(bits[index].count('1') < len(bits[index])/2)

print(int(gamma_rate, 2) * int(epsilon_rate, 2))