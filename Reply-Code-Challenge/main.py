class Demon:
    def __init__(self, stamina_points, turns, recover_stamina, fragments_list):
        self.stamina_points = stamina_points
        self.turns = turns
        self.recover_stamina = recover_stamina
        try:
            fragments_list.remove('')
        except Exception:
            pass
        self.fragments_list = [int(x) for x in fragments_list]
        self.stamina_heur_points = self.stamina_heur()

    def __str__(self):
        return 'Demon(stamina_points=' + str(
            self.stamina_points) + ', turns=' + str(self.turns) + ', recover_stamina=' + str(
            self.recover_stamina) + ',fragments_list=' + str(self.fragments_list) + ') '

    def stamina_heur(self):
        return self.recover_stamina / self.turns - self.stamina_points

    def fragm_heur(self, current_turn):
        left_turns = self.turns - current_turn
        score = 0
        for i in range(min(left_turns, len(self.fragments_list) - 1)):
            score += self.fragments_list[i]
        return score


if __name__ == '__main__':
    # file_input = open("00-example.txt", "r")
    file_input = open("05-androids-armageddon.txt", "r")
    # file_input = open("04-the-desert-of-autonomous-machines.txt", "r")
    # file_input = open("03-etheryum.txt", "r")
    # file_input = open("02-iot-island-of-terror.txt", "r")
    #file_input = open("01-the-cloud-abyss.txt", "r")
    data = file_input.read()

    data = data.split("\n")
    data_in = data.pop(0)
    data_in = data_in.split(" ")

    stamina = int(data_in[0])
    max_stamina = data_in[1]
    max_turns = data_in[2]
    number_of_demons = data_in[3]

    # print(data)
    demons = []
    i = 0
    for demon in data:
        if demon == '':
            break
        demon_data = demon.split(" ")
        # print(demon_data)
        demons.append((i, Demon(int(demon_data[0]), int(demon_data[1]), int(demon_data[2]), demon_data)))
        i += 1

    path = "05-androids-armageddon-out.txt"
    g = open(path, "w")
    # demons.sort(key=lambda x: x[1].stamina_heur_points, reverse=True)
    # demons.sort(key=lambda x: x[1].fragm_heur(0), reverse=True)
    # d_st = sorted(demons, key=lambda x: x[1].stamina_heur_points, reverse=True)
    # d_fr = sorted(demons, key=lambda x: x[1].fragm_heur(0), reverse=True)
    for i in range(int(max_turns)):
        d_fr = sorted(demons, key=lambda x: x[1].fragm_heur(i), reverse=True)
        ind = 0
        demon = d_fr[ind]
        if demon[1].stamina_heur_points > stamina:
            #while demon[1].stamina_heur_points > stamina and ind < len(demons):
            ind += 1
        # else:
        #     stamina -= demon[1].stamina_heur_points
        g.write(str(demon[0]) + '\n')
        demons.remove(demon)
    g.close()
