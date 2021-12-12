# simulator for fleet battles

# class type
class Ship:
    position = 0
    status = 'destroyed' 
    model = 'blank' 
    tonnage = 0
    armour = [0, 'blank']
    shields = 0
    thrusters = 0
    munitions = 'blank'
    weaponry = [0, 0, 0, 'blank']
    crew = 'blank'
    experience = [0, 'blank']
    insignia = 'b'
    name = 'blank'

    def __init__(self, position, status, model,tonnage,armour,shields,thrusters,munitions,weaponry,crew,experience,insignia,name):
        self.position = position
        self.status = status
        self.model = model
        self.tonnage = tonnage
        self.armour = armour
        self.shields = shields
        self.thrusters = thrusters
        self.munitions = munitions
        self.weaponry = weaponry
        self.crew = crew
        self.experience = experience
        self.insignia = insignia
        self.name = name

# damage calculations
def weapon_damage(o_model,o_munitions,o_weaponry,o_experience,o_name,  t_position,t_model,t_tonnage,t_armour,t_shields,t_thrusters,t_experience,t_name):
    """calculates weapon damage"""
    import random
    splash = False
    shot_num = 0
    hull_damage = 0
    hit_spot = None
    shots = o_weaponry[0]
    while shots > 0 and t_tonnage > 0:
        hit = False
        armour_cover = False
        hit_chance = random.randint(-1,9)
        damage_variance = random.uniform(0.8, 1.2)
        shot_num += 1
        if o_munitions == 'scrap':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 7:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*1.2*damage_variance
                    if t_shields < damage:
                        hull_damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//2) - t_shields
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*0.8*damage_variance:
                    hit_spot = 'armour'
                    damage = o_weaponry[1]*0.8*damage_variance - (t_armour[0])
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//2)

        elif o_munitions == 'missile':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 11:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*1*damage_variance
                    if t_shields < damage:
                        hull_damage = o_weaponry[1]*1.2*damage_variance - (t_armour[0]//2) - t_shields
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*1.5*damage_variance:
                    hit_spot = 'armour'
                    damage = o_weaponry[1]*1.2*damage_variance - (t_armour[0])
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//2)

        elif o_munitions == 'coilgun':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 9:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*1.4*damage_variance
                    if t_shields < damage:
                        hull_damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//2) - t_shields
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*1*damage_variance:
                    hit_spot = 'armour'
                    damage = o_weaponry[1]*1*damage_variance - (t_armour[0])
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//2)

        elif o_munitions == 'laser':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 12:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*0.8*damage_variance
                    if t_shields < damage:
                        hull_damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//2) - t_shields
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*0.9*damage_variance:
                    hit_spot = 'armour'
                    damage = o_weaponry[1]*0.9*damage_variance - (t_armour[0])
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//2)

        elif o_munitions == 'plasma':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 9:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*0.9*damage_variance
                    if t_shields < damage:
                        hull_damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//3) - t_shields
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*1.6*damage_variance:
                    hit_spot = 'armour'
                    damage = o_weaponry[1]*1.25*damage_variance - (t_armour[0])
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//3)

        elif o_munitions == 'strike-craft':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 13:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*1*damage_variance
                    if t_shields < damage:
                        hull_damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//2) - t_shields
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*0.7*damage_variance:
                    hit_spot = 'armour'
                    damage = o_weaponry[1]*0.7*damage_variance - (t_armour[0])
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//2)

        elif o_munitions == 'heavy gunz':
           if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 9:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*1.6*damage_variance
                    if t_shields < damage:
                        hull_damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//2) - t_shields
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*1.2*damage_variance:
                    hit_spot = 'armour'
                    damage = o_weaponry[1]*1*damage_variance - (t_armour[0])
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//2)

        elif o_munitions == 'ripper claw':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 9:
                hit = True
                if t_armour[0] > o_weaponry[1]*1*damage_variance:
                    hit_spot = 'armour'
                    damage = o_weaponry[1]*1*damage_variance - (t_armour[0])
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//2)

        elif o_munitions == 'bio-acid':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 9:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*0.7*damage_variance
                    if t_shields < damage:
                        hull_damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//3) - t_shields
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*1.4*damage_variance:
                    hit_spot = 'armour'
                    damage = o_weaponry[1]*1.15*damage_variance - (t_armour[0])
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance - (t_armour[0]//3)
  
        elif o_munitions == 'marines':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 9:
                hit = True
                hit_spot = 'hull'
                damage = o_weaponry[1]*1*damage_variance

        elif o_munitions == 'daemon':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 9:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*0.6*damage_variance
                    if t_shields < damage:
                        hull_damage = o_weaponry[1]*1.6*damage_variance - (t_armour[0]//2) - t_shields
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*0.8*damage_variance:
                    hit_spot = 'armour'
                    damage = o_weaponry[1]*0.8*damage_variance - (t_armour[0])
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1.6*damage_variance - (t_armour[0]//2)

        elif o_munitions == 'lance':
           if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 11:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*1*damage_variance
                    if t_shields < damage:
                        hull_damage = o_weaponry[1]*1.2*damage_variance - (t_armour[0]//2) - t_shields
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*1.6*damage_variance:
                    hit_spot = 'armour'
                    damage = o_weaponry[1]*1.4*damage_variance - (t_armour[0])
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1.2*damage_variance - (t_armour[0]//2)

        elif o_munitions == 'nova cannon':
           if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 16:
                splash = True
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*1*damage_variance
                    if t_shields < damage:
                        hull_damage = o_weaponry[1]*1.5*damage_variance - (t_armour[0]//2) - t_shields
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*2*damage_variance:
                    hit_spot = 'armour'
                    damage = o_weaponry[1]*1.6*damage_variance - (t_armour[0])
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1.5*damage_variance - (t_armour[0]//2)

        shots -= 1           
        if splash == True and hit == False:
            print(f"{'The explosion from ' + o_name + chr(39) + 's ' + o_munitions + ' misses ' + t_name + '!':<100}"                                                                                             f"{'('+o_model + ' firing on ' + t_model + ')':>15}")               
        elif splash == True and armour_cover == True:
            if damage <= 0:
                print(f"{'The explosion from ' + o_name + chr(39) + 's ' + o_munitions + ' washes over the ' + t_name + str(chr(39)) + 's armour, dealing no damage.':<100}"                                 f"{'('+o_model + ' firing on ' + t_model + ')':>15}")
            elif damage > 0:
                print(f"{'The explosion from ' + o_name + chr(39) + 's ' + o_munitions + ' is partly blocked by the ' + t_name + str(chr(39)) + 's armour, dealing ' + str(round(damage)) + ' damage.':<100}"                                 f"{'('+o_model + ' firing on ' + t_model + ')':>15}")
        elif splash == True:
            t_tonnage -= damage
            print(f"{'The explosion from ' + o_name + chr(39) + 's ' + o_munitions + ' has hit the ' + t_name + str(chr(39)) + 's ' + hit_spot + ' for ' + str(round(damage)) + ' damage.':<100}"         f"{'('+o_model + ' firing on ' + t_model +')':>15}")

        elif hit == False:
            print(f"{'Shot ' + str(shot_num) + ' from ' + o_name + ' misses ' + t_name + '!':<100}"                                                                                             f"{'('+o_model + ' firing on ' + t_model + ')':>15}")
        elif armour_cover == True:
            if damage <= 0:
                print(f"{o_name + chr(39) + 's ' + o_munitions + ' fire glances off the ' + t_name + str(chr(39)) + 's armour, dealing no damage.':<100}"                                 f"{'('+o_model + ' firing on ' + t_model + ')':>15}")
            elif damage > 0:
                print(f"{o_name + chr(39) + 's ' + o_munitions + ' fire is partly blocked by the ' + t_name + str(chr(39)) + 's armour, dealing ' + str(round(damage)) + ' damage.':<100}"                                 f"{'('+o_model + ' firing on ' + t_model + ')':>15}")
        else:
            t_tonnage -= damage
            print(f"{o_name + chr(39) + 's ' + o_munitions + ' fire has hit the ' + t_name + str(chr(39)) + 's ' + hit_spot + ' for ' + str(round(damage)) + ' damage.':<100}"         f"{'('+o_model + ' firing on ' + t_model +')':>15}")
        if hit_spot == 'shields' and hull_damage > 0:
            print(f'The shot has broken through the shield and does {round(hull_damage)} to the hull!')

    print(f'{t_name} has {round(t_tonnage)} structural integrity left!')

    return t_tonnage




def combat_movement(linelist, fleet1, fleet2, fleet1_zone_dict, fleet2_zone_dict, turn):
    for ship in fleet1:
        if ship.status == 'destroyed' and ship.model != 'blank':
            linelist[ship.position+1] = linelist[ship.position+1][0:fleet1.index(ship)+6]  +'#'+ linelist[ship.position+1][fleet1.index(ship)+7:]
        elif ship.model != 'blank':
            linelist[ship.position+1] = linelist[ship.position+1][0:fleet1.index(ship)+6] + ship.insignia + linelist[ship.position+1][fleet1.index(ship)+7:]
        if turn != 0 and ship.model != 'blank':
            linelist[ship.position-ship.thrusters//3] = linelist[ship.position-ship.thrusters//3][0:fleet1.index(ship)+6]  +'-'+ linelist[ship.position-ship.thrusters//3][fleet1.index(ship)+7:]
    
    for ship in fleet2:
        if ship.status == 'destroyed' and ship.model != 'blank':
            linelist[ship.position+1] = linelist[ship.position+1][0:fleet2.index(ship)+5]  +'#'+ linelist[ship.position+1][fleet2.index(ship)+6:]
        elif ship.model != 'blank':
            linelist[ship.position+1] = linelist[ship.position+1][0:fleet2.index(ship)+5]  + ship.insignia + linelist[ship.position+1][fleet2.index(ship)+6:]
        if turn != 0 and ship.model != 'blank':
            linelist[ship.position+2+ship.thrusters//3] = linelist[ship.position+2+ship.thrusters//3][0:fleet2.index(ship)+5]  +'-'+ linelist[ship.position+2+ship.thrusters//3][fleet2.index(ship)+6:]



    return linelist

def combat_grid(fleet1,fleet2):
    if len(fleet1) < len(fleet2):
        width = len(fleet2) + 7
    else:
        width = len(fleet1) + 7
    if width % 2 != 0:
        width += 1
    start_barrier = '╔'+(width)*'═'+'╗'
    end_barrier = '╚'+(width)*'═'+'╝'
    linelist = []

    linelist.append(start_barrier)
    for i in range(13):
        linelist.append('║'+width*'-'+'║')
    linelist.append(end_barrier)
    return linelist

def fleet_combat(fleet1,fleet2):
    import random
    import math
    import itertools
    blank = Ship
    print(len(fleet1))
    print(len(fleet2))

    if len(fleet1) < len(fleet2):
        blank_fleet = len(fleet2)//3.5
        print(blank_fleet)
        while blank_fleet > 0:
            fleet1.insert(0, blank)
            blank_fleet -= 1

    elif len(fleet2) < len(fleet1):
        blank_fleet = len(fleet1)//3.5
        while blank_fleet > 0:
            fleet2.insert(0, blank)
            blank_fleet -= 1

    print(len(fleet1))
    print(len(fleet2))
    linelist = combat_grid(fleet1,fleet2)
    fleet1_zone_dict = {}
    fleet2_zone_dict = {}
    for ship in fleet1:
        fleet1_zone_dict[ship] = 0
        ship.position = 0
    for ship in fleet2:
        fleet2_zone_dict[ship] = 12
        ship.position = 12
    turn = 0
    linelist = combat_movement(linelist, fleet1, fleet2, fleet1_zone_dict, fleet2_zone_dict, turn)
    active_flag = True
    print('\n'.join(linelist))
    input(f'Game start!')

    while active_flag == True:
        for ship1, ship2 in itertools.zip_longest(fleet1, fleet2):
            ship1_move_counter = True
            ship2_move_counter = True
            if ship1 != None and len(fleet2) != 0 and ship1.tonnage > 0 and ship1.status == 'functional':
                firing_list1 = []
                for ship in fleet2:
                    if ship.status == 'functional' and abs(ship.position - ship1.position) <= 2 + ship1.weaponry[2]:
                        firing_list1.append(fleet2.index(ship))
                        ship1_move_counter = False

                if len(firing_list1) == 0:
                    ship1_move_counter = True

                if ship1_move_counter == True:
                    print(f'{ship1.name} advances on the enemy.')
                    ship1.position += (1 + ship1.thrusters//3)

                elif len(firing_list1) != 0:
                    t_ship = random.choice(firing_list1)
                

                    if ship1_move_counter == False:
                        fleet2[t_ship].tonnage = weapon_damage(ship1.model,ship1.munitions,ship1.weaponry,ship1.experience,ship1.name,  fleet2[t_ship].position,fleet2[t_ship].model,fleet2[t_ship].tonnage,fleet2[t_ship].armour,fleet2[t_ship].shields,fleet2[t_ship].thrusters,fleet2[t_ship].experience,fleet2[t_ship].name)
                        if ship1.munitions == 'nova cannon':
                            if t_ship - 1 < len(fleet2):
                                fleet2[t_ship - 1].tonnage = weapon_damage(ship1.model,ship1.munitions,ship1.weaponry,ship1.experience,ship1.name,  fleet2[t_ship - 1].position, fleet2[t_ship - 1].model,fleet2[t_ship - 1].tonnage,fleet2[t_ship - 1].armour,fleet2[t_ship - 1].shields,fleet2[t_ship - 1].thrusters,fleet2[t_ship - 1].experience,fleet2[t_ship - 1].name)                                
                            if t_ship + 1 < len(fleet2):
                                fleet2[t_ship + 1].tonnage = weapon_damage(ship1.model,ship1.munitions,ship1.weaponry,ship1.experience,ship1.name,  fleet2[t_ship + 1].position, fleet2[t_ship + 1].model,fleet2[t_ship + 1].tonnage,fleet2[t_ship + 1].armour,fleet2[t_ship + 1].shields,fleet2[t_ship + 1].thrusters,fleet2[t_ship + 1].experience,fleet2[t_ship + 1].name)                                

            for ship in fleet2:
                if ship.tonnage <= 0 and ship.status == 'functional':
                    print(f'{ship.name} ({ship.crew} {ship.model}) has been destroyed!')
                    ship.status = 'destroyed'
                    break

            if ship2 != None and len(fleet1) != 0 and ship2.tonnage > 0 and ship2.status == 'functional': 
                firing_list2 = []
                for ship in fleet1:
                        
                    if ship.status == 'functional' and abs(ship.position - ship2.position) <= 2 +  ship2.weaponry[2]:
                        firing_list2.append(fleet1.index(ship))
                        ship2_move_counter = False

                if len(firing_list2) == 0:
                    ship1_move_counter = True

                if ship2_move_counter == True:
                    print(f'{ship2.name} advances on the enemy.')
                    ship2.position -= (1 + ship2.thrusters//3)

                elif len(firing_list2) != 0:
                    t_ship = random.choice(firing_list2)


                    if ship2_move_counter == False:
                        fleet1[t_ship].tonnage = weapon_damage(ship2.model,ship2.munitions,ship2.weaponry,ship2.experience,ship2.name,  fleet1[t_ship].position, fleet1[t_ship].model,fleet1[t_ship].tonnage,fleet1[t_ship].armour,fleet1[t_ship].shields,fleet1[t_ship].thrusters,fleet1[t_ship].experience,fleet1[t_ship].name)
                        if ship2.munitions == 'nova cannon':
                            if t_ship - 1 < len(fleet1):
                                fleet1[t_ship - 1].tonnage = weapon_damage(ship2.model,ship2.munitions,ship2.weaponry,ship2.experience,ship2.name,  fleet1[t_ship - 1].position, fleet1[t_ship - 1].model,fleet1[t_ship - 1].tonnage,fleet1[t_ship - 1].armour,fleet1[t_ship - 1].shields,fleet1[t_ship - 1].thrusters,fleet1[t_ship - 1].experience,fleet1[t_ship - 1].name)                                
                            if t_ship + 1 < len(fleet1):
                                fleet1[t_ship + 1].tonnage = weapon_damage(ship2.model,ship2.munitions,ship2.weaponry,ship2.experience,ship2.name,  fleet1[t_ship + 1].position, fleet1[t_ship + 1].model,fleet1[t_ship + 1].tonnage,fleet1[t_ship + 1].armour,fleet1[t_ship + 1].shields,fleet1[t_ship + 1].thrusters,fleet1[t_ship + 1].experience,fleet1[t_ship + 1].name)                                

            for ship in fleet1:
                if ship.tonnage <= 0 and ship.status == 'functional':
                    print(f'{ship.name} ({ship.crew} {ship.model}) has been destroyed!')
                    ship.status = 'destroyed'
                    break


                        
        turn += 1      
        linelist = combat_movement(linelist, fleet1, fleet2, fleet1_zone_dict, fleet2_zone_dict, turn)
        print('\n'.join(linelist))      


        end_flag1 = False
        end_flag2 = False
        for ship in fleet1:
            if ship.status == 'destroyed':
                end_flag1 = True
            else:
                end_flag1 = False
                break
                
        for ship in fleet2:
            if ship.status == 'destroyed':
                end_flag2 = True
            else:
                end_flag2 = False
                break
        
        if end_flag1 == True:
            print('Fleet 2 wins!')
            active_flag = False
        if end_flag2 == True:
            print('Fleet 2 wins!')
            active_flag = False

        input(f'Round {turn} round ends')

    linelist = combat_movement(linelist, fleet1, fleet2, fleet1_zone_dict, fleet2_zone_dict, turn)
    print('\n'.join(linelist)) 
    return fleet1, fleet2

def fleet_loader(fleet_file):
    fleet_list = []
    with open (fleet_file, 'r') as fleet:
        for ship in fleet:
            ship = ship.strip('\n').replace(' ', '').replace(',', ' ').split('.') 

            ship[0] = Ship(int(ship[1]), ship[2],ship[3], int(ship[4]), [int(ship[5]),ship[6]], int(ship[7]), int(ship[8]), ship[9], [int(ship[10]),int(ship[11]),int(ship[12]),ship[13]], ship[14], [int(ship[15]),ship[16]], ship[17], ship[18])
            fleet_list.append(ship[0])
    return fleet_list

def start_up(fleet):
    fleet_dict = {}
    for ship in fleet:
        if ship.model in fleet_dict:
            fleet_dict[ship.model] += 1
        else:
            fleet_dict[ship.model] = 1
    return fleet_dict

fleet1 = fleet_loader('fleet1.txt')
fleet2 = fleet_loader('fleet1.txt')