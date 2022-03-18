f = open("../input.txt", 'r')
lines = f.readlines()
data = []
for line in lines:
    data.append(line[:-1])  # ignore the newline

print("data:" + str(data))


def boolString(bool_var):
    if bool_var:
        return "1"
    else:
        return "0"


selected_for_O = data
selected_for_CO2 = data
for index in range(12):
    if len(selected_for_O) == 1 and len(selected_for_CO2) == 1:
        print(index)
        break
    current_significant_bits_O = list(map(lambda x: x[index], selected_for_O))
    current_significant_bits_CO2 = list(map(lambda x: x[index], selected_for_CO2))
    max_occ_O = boolString(current_significant_bits_O.count('1') >= len(current_significant_bits_O) / 2)
    max_occ_CO2 = boolString(current_significant_bits_CO2.count('1') < len(current_significant_bits_CO2) / 2)
    if len(selected_for_O) > 1:
        selected_for_O = list(filter(lambda x: x[index] == max_occ_O, selected_for_O))
    if len(selected_for_CO2) > 1:
        selected_for_CO2 = list(filter(lambda x: x[index] == max_occ_CO2, selected_for_CO2))

print(int(selected_for_O[0], 2) * int(selected_for_CO2[0], 2))
