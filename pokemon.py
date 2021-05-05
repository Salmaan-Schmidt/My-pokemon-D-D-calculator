import pandas as pd
import sys

pokemon_stats = pd.read_csv("pokemon.csv")
pokemon_moves = pd.read_csv("pokemon_move.csv")

while True:
    pokemon_name = input("Pokemon name: ")
    filter_name = pokemon_stats.loc[pokemon_stats["Name"] == pokemon_name,"HP"]
    if filter_name.empty:
        print(pokemon_name + " not found")
        continue
    else:
        break

pokemon_lvl = int(input("insert pokemon lvl: "))
pokemon_hp = pokemon_stats.loc[pokemon_stats["Name"] == pokemon_name,"HP"]
pokemon_def = pokemon_stats.loc[pokemon_stats["Name"] == pokemon_name,"Defense"]
pokemon_sp_def = pokemon_stats.loc[pokemon_stats["Name"] == pokemon_name,"Sp. Def"]
pokemon_speed = pokemon_stats.loc[pokemon_stats["Name"] == pokemon_name,"Speed"]
pokemon_att = pokemon_stats.loc[pokemon_stats["Name"] == pokemon_name,"Attack"]
pokemon_sp_att = pokemon_stats.loc[pokemon_stats["Name"] == pokemon_name,"Sp. Atk"]
# print(len(sys.argv))


def basic_stat_calc():
    """Takes user input to calculate the output for the stat block"""
    hp = int(((pokemon_hp*0.1)*3)+pokemon_lvl)
    dex = int(((pokemon_speed+pokemon_lvl)*0.1)/2)
    ac = int(((pokemon_def+pokemon_lvl)*0.1)/2)
    sac = int(((pokemon_sp_def+pokemon_lvl)*0.1)/2)
    return hp,dex,ac,sac


def show_calc(hp,dex,ac,sac,move_list):
    if len(sys.argv) > 1:
        title = sys.argv[1]
    else:
        title = "pokemon_test"
    with open(title+".txt","a") as f:
        f.write(pokemon_name+"\n")
        f.write("\n")
        f.write("HP: "+ str(hp)+ "\n")
        f.write("DEX: "+ str(dex)+"\n")
        f.write("AC : "+ str(ac)+"\n")
        f.write("SAC: "+ str(sac)+"\n")
        for x in move_list:
            f.write(x+"\n")
        f.write("\n")


def move_calc():
    """coverts the pokemon move power and translates it to dnd damage roll """
    move_list = []
    for x in range(4):
        try:
            power = int(input("insert attack power "))
        except ValueError:
            continue
        
        # while True:
        #     pokemon_move_name = input("Name of pokemon moves: ")
        #     filter_name = pokemon_stats.loc[pokemon_stats["identifier"] == pokemon_move_name,"power"]
        #     if filter_name.empty:
        #         print(pokemon_move_name + " not found")
        #         continue
        #     else:
        #         break

        pokemon_move_name = input("Name of pokemon moves: ")
        flag = input("Is the Pokemon move type same as pokemon type [y/n] ")
        if flag == 'y' or flag == 'Y':
            stb = 1
        elif flag == 'n' or flag == 'N':
            stb = 0

        
        flag1 = input("Is the Pokemon move a special or physical move [p/s]")
        if flag1 == 's' or flag1 == 'S':
            att = int(((pokemon_att+pokemon_lvl)*0.1)/2)
        elif flag1 == 'p' or flag1 == 'P':
            att = int(((pokemon_sp_att+pokemon_lvl)*0.1)/2)


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
    # print(pokemon_moves.head())
    # print(filter_name.head())
    # print(filter_name*5)
    
