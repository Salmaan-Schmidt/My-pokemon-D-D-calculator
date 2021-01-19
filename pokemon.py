import sys


pokemon_name = input("Pokemon name: ")
pokemon_lvl = int(input("insert pokemon lvl: "))
pokemon_hp = int(input("insert base HP: "))
pokemon_def = int(input("insert base def: "))
pokemon_sp_def = int(input("insert base sp def: "))
pokemon_speed = int(input("insert base speed: "))
pokemon_att = int(input("insert base att: "))
pokemon_sp_att = int(input("insert base sp att: "))
# print(len(sys.argv))

def basic_stat_calc():
    """Takes user input to calculate the output for the stat block"""
    hp = int(((pokemon_hp*0.1)*3)+pokemon_lvl)
    dex = int((pokemon_speed*0.1)/2)
    ac = int((pokemon_def*0.1)/2)
    sac = int((pokemon_sp_def*0.1)/2)
    return hp,dex,ac,sac


def show_calc(hp,dex,ac,sac,move_list):
    if len(sys.argv) > 1:
        title = sys.argv[1]
    else:
        title = "pokemon_test"
    with open(title+".txt","a") as f
        f.write(pokemon_name+"\n")
        f.write("\n")
        f.write("HP: "+ str(hp)+ "\n")
        f.write("DEX: "+ str(dex)+"\n")
        f.write("AC : "+ str(ac)+"\n")
        f.write("SAC: "+ str(sac)+"\n")
        for x in move_list:
            f.write(x+"\n")
        f.write("\n")
#     f.close()
    # print("HP: ",hp)
    # print("DEX: ",dex)
    # print("AC : ",ac)
    # print("SAC: ",sac)
    # for x in move_list:
    #     print(x)


def move_calc():
    """coverts the pokemon move power and translates it to dnd damage roll """
    move_list = []
    for x in range(4):
        try:
            power = int(input("insert attack power "))
        except ValueError:
            continue
        
        pokemon_move_name = input("Name of pokemon moves: ")
        flag = input("Is the Pokemon move type same as pokemon type [y/n] ")
        if flag == 'y' or flag == 'Y':
            stb = 1
        elif flag == 'n' or flag == 'N':
            stb = 0

        
        flag1 = input("Is the Pokemon move a special or physical move [p/s]")
        if flag1 == 's' or flag1 == 'S':
            att = int((pokemon_att*0.1)/2)
        elif flag1 == 'p' or flag1 == 'P':
            att = int((pokemon_sp_att*0.1)/2)


        if power >= 40  and power < 60:
            if 60-power == 5:
                x = 3
                move_list.append((pokemon_move_name+' 1D8 + '+ str(x+att+stb)))
            elif 60-power == 15:
                x = 1
                move_list.append((pokemon_move_name+' 1D8 + '+ str(x+att+stb)))
            elif 60-power == 10:
                x = 2
                move_list.append((pokemon_move_name+' 1D8 + '+ str(x+att+stb)))
            else:
                move_list.append((pokemon_move_name+' 1D8 + '+ str(att+stb)))


        if power >= 60 and power < 80:
            if 80-power == 5:
                x = 3
                move_list.append((pokemon_move_name +' 1D10 + '+ str(x+att+stb)))
            elif 80-power == 15:
                x = 1
                move_list.append((pokemon_move_name+' 1D10 + '+ str(x+att+stb)))
            elif 80-power == 10:
                x = 2
                move_list.append((pokemon_move_name+' 1D10 + '+ str(x+att+stb)))
            else:
                move_list.append((pokemon_move_name+' 1D10 + '+ str(att+stb)))
        

        if power >= 80 and power < 100:
            if 100-power == 5:
                x = 3
                move_list.append((pokemon_move_name+' 1D12 + '+ str(x+att+stb)))
            elif 100-power == 15:
                x = 1
                move_list.append((pokemon_move_name+' 1D12 + '+ str(x+att+stb)))
            elif 100-power == 10:
                x = 2
                move_list.append((pokemon_move_name+' 1D12 + '+ str(x+att+stb)))
            else:
                move_list.append((pokemon_move_name+' 1D12 + '+ str(att+stb)))
        

        if power >= 100 and power < 120:
            if 120-power == 5:
                x = 3
                move_list.append((pokemon_move_name+' 1D12 + 1D4 + '+ str(x+att+stb)))
            elif 120-power == 15:
                x = 1
                move_list.append((pokemon_move_name+' 1D12 + 1D4 + '+ str(x+att+stb)))
            elif 120-power == 10:
                x = 2
                move_list.append((pokemon_move_name+' 1D12 + 1D4 + '+ str(x+att+stb)))
            else:
                move_list.append((pokemon_move_name+' 1D12 + 1D4 + '+ str(att+stb)))


        if power >= 120 and power < 140:
            if 140-power == 5:
                x = 3
                move_list.append((pokemon_move_name+' 1D12 + 1D6 + '+ str(x+att+stb)))
            elif 140-power == 15:
                x = 1
                move_list.append((pokemon_move_name+' 1D12 + 1D6 + '+ str(x+att+stb)))
            elif 140-power == 10:
                x = 2
                move_list.append((pokemon_move_name+' 1D12 + 1D6 + '+ str(x+att+stb)))
            else:
                move_list.append((pokemon_move_name+' 1D12 + 1D6 + '+ str(att+stb)))
    return move_list


if __name__ == '__main__':
    hp,dex,ac,sac = basic_stat_calc()
    move_list = move_calc()
    show_calc(hp,dex,ac,sac,move_list)
    
