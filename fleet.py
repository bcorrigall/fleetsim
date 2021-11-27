# simulator for fleet battles

# class type
class Ship:
    def __init__(self,model,tonnage,armour,shields,thrusters,munitions,weaponry,crew,experience,name):
        self.model = model
        self.tonnage = tonnage
        self.armour = armour
        self.shields = shields
        self.thrusters = thrusters
        self.munitions = munitions
        self.weaponry = weaponry
        self.crew = crew
        self.experience = experience
        self.name = name

# damage calculations
def weapon_damage(o_model,o_munitions,o_weaponry,o_experience,o_name,  t_model,t_tonnage,t_armour,t_shields,t_thrusters,t_experience,t_name):
    """calculates weapon damage"""
    import random
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
                        hull_damage = (damage - t_shields)*1*damage_variance + (t_armour[0]//2)
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*0.8*damage_variance:
                    hit_spot = 'armour'
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance + (t_armour[0]//2)
                    t_tonnage -= damage
        elif o_munitions == 'missile':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 11:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*1*damage_variance
                    if t_shields < damage:
                        hull_damage = (damage - t_shields)*1*damage_variance + (t_armour[0]//2)
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*1.5*damage_variance:
                    hit_spot = 'armour'
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance + (t_armour[0]//2)
                    t_tonnage -= damage
        elif o_munitions == 'coilgun':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 9:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*1.4*damage_variance
                    if t_shields < damage:
                        hull_damage = (damage - t_shields)*1*damage_variance + (t_armour[0]//2)
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*1*damage_variance:
                    hit_spot = 'armour'
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance + (t_armour[0]//2)
                    t_tonnage -= damage
        elif o_munitions == 'laser':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 12:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*0.8*damage_variance
                    if t_shields < damage:
                        hull_damage = (damage - t_shields)*1*damage_variance + (t_armour[0]//2)
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*0.9*damage_variance:
                    hit_spot = 'armour'
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance + (t_armour[0]//2)
                    t_tonnage -= damage
        elif o_munitions == 'plasma':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 9:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*0.9*damage_variance
                    if t_shields < damage:
                        hull_damage = (damage - t_shields)*1*damage_variance + (t_armour[0]//3)
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*1.6*damage_variance:
                    hit_spot = 'armour'
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance + (t_armour[0]//3)
                    t_tonnage -= damage
        elif o_munitions == 'strike-craft':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 13:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*1*damage_variance
                    if t_shields < damage:
                        hull_damage = (damage - t_shields)*1*damage_variance + (t_armour[0]//2)
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*0.7*damage_variance:
                    hit_spot = 'armour'
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance + (t_armour[0]//2)
                    t_tonnage -= damage
        elif o_munitions == 'heavy gunz':
           if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 11:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*1.6*damage_variance
                    if t_shields < damage:
                        hull_damage = (damage - t_shields)*1*damage_variance + (t_armour[0]//2)
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*1.2*damage_variance:
                    hit_spot = 'armour'
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance + (t_armour[0]//2)
                    t_tonnage -= damage
        elif o_munitions == 'ripper claw':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 9:
                hit = True
                if t_armour[0] > o_weaponry[1]*1*damage_variance:
                    hit_spot = 'armour'
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance + (t_armour[0]//2)
                    t_tonnage -= damage
        elif o_munitions == 'bio-acid':
            if (hit_chance + t_thrusters + t_experience[0] - o_experience[0]) < 9:
                hit = True
                if t_shields > 0:
                    hit_spot = 'shields'
                    damage = o_weaponry[1]*0.7*damage_variance
                    if t_shields < damage:
                        hull_damage = (damage - t_shields)*1*damage_variance + (t_armour[0]//3)
                        t_tonnage -= hull_damage
                    t_shields -= damage
                elif t_armour[0] > o_weaponry[1]*1.4*damage_variance:
                    hit_spot = 'armour'
                    armour_cover = True
                else:
                    hit_spot = 'hull'
                    damage = o_weaponry[1]*1*damage_variance + (t_armour[0]//3)
                    t_tonnage -= damage

        shots -= 1                                   
        if hit == False:
            print(f"{'Shot ' + str(shot_num) + ' from ' + o_name + ' misses ' + t_name + '!':<90}"                                                                                             f"{'('+o_model + ' firing on ' + t_model + ')':>15}")
        elif armour_cover == True:
            print(f"{o_name + chr(39) + 's ' + o_munitions + ' fire bounces off the ' + t_name + str(chr(39)) + 's armour for 0 hull damage.':<90}"                                 f"{'('+o_model + ' firing on ' + t_model + ')':>15}")
        else:
            print(f"{o_name + chr(39) + 's ' + o_munitions + ' fire has hit the ' + t_name + str(chr(39)) + 's ' + hit_spot + ' for ' + str(round(damage)) + ' damage.':<90}"         f"{'('+o_model + ' firing on ' + t_model +')':>15}")
        if hit_spot == 'shields' and hull_damage > 0:
            print(f'The shot has broken through the shield and does {round(hull_damage)} to the hull!')

    print(f'{t_name} has {round(t_tonnage)} structural integrity left!')

    return t_tonnage


def fleet_combat(fleet1,fleet2):
    import random
    import math
    import itertools
    fleet1_zone_dict = {}
    fleet2_zone_dict = {}
    for ship in fleet1:
        fleet1_zone_dict[ship] = 0
    for ship in fleet2:
        fleet2_zone_dict[ship] = 12
    turn = 0
    active_flag = True
    while active_flag == True:
        for ship1, ship2 in itertools.zip_longest(fleet1, fleet2):
            ship1_move_counter = False
            ship2_move_counter = False
            if ship1 != None and len(fleet2) != 0 and ship1.tonnage > 0:
                for ship in fleet2_zone_dict:
                    if abs(fleet2_zone_dict[ship] - fleet1_zone_dict[ship1]) > 3 + ship1.weaponry[2]:
                        fleet1_zone_dict[ship1] += (1 + ship1.thrusters//3)
                        ship1_move_counter = True
                        print(f'{ship1.name} advances on the enemy.')
                        break
                if len(fleet2) == 1:
                    t_ship = 0
                else:
                    t_ship = random.randint(0, len(fleet2)-1)
                if ship1_move_counter == False:
                    fleet2[t_ship].tonnage = weapon_damage(ship1.model,ship1.munitions,ship1.weaponry,ship1.experience,ship1.name,  fleet2[t_ship].model,fleet2[t_ship].tonnage,fleet2[t_ship].armour,fleet2[t_ship].shields,fleet2[t_ship].thrusters,fleet2[t_ship].experience,fleet2[t_ship].name)

            if ship2 != None and len(fleet1) != 0 and ship2.tonnage > 0: 
                for ship in fleet1_zone_dict:
                    if abs(fleet1_zone_dict[ship] - fleet2_zone_dict[ship2]) > 3 + ship2.weaponry[2]:
                        fleet2_zone_dict[ship2] -= (1 + ship2.thrusters//3)
                        ship2_move_counter = True
                        print(f'{ship2.name} advances on the enemy.')
                        break
                if len(fleet1) == 1:
                    t_ship = 0
                else:
                    t_ship = random.randint(0, len(fleet1)-1)
                if ship2_move_counter == False:
                    fleet1[t_ship].tonnage = weapon_damage(ship2.model,ship2.munitions,ship2.weaponry,ship2.experience,ship2.name,  fleet1[t_ship].model,fleet1[t_ship].tonnage,fleet1[t_ship].armour,fleet1[t_ship].shields,fleet1[t_ship].thrusters,fleet1[t_ship].experience,fleet1[t_ship].name)

            for ship in fleet1:
                if ship.tonnage <= 0:
                    print(f'{ship.name} ({ship.crew} {ship.model}) has been destroyed!')
                    fleet1.pop(fleet1.index(ship))
                    break
            for ship in fleet2:
                if ship.tonnage <= 0:
                    print(f'{ship.name} ({ship.crew} {ship.model}) has been destroyed!')
                    fleet2.pop(fleet2.index(ship))
                    break


        turn += 1            
        input(f'Round {turn} round ends')

        if not fleet1:
            print('Fleet 2 wins!')
            break
        if not fleet2:
            print('Fleet 1 wins!')
            break

    return fleet1, fleet2

def fleet_loader(fleet_file):
    fleet_list = []
    with open (fleet_file, 'r') as fleet:
        for ship in fleet:
            ship = ship.strip('\n').replace(' ', '').replace(',', ' ').split('.') 

            ship[0] = Ship(ship[1], int(ship[2]), [int(ship[3]),ship[4]], int(ship[5]), int(ship[6]), ship[7], [int(ship[8]),int(ship[9]),int(ship[10]),ship[11]], ship[12], [int(ship[13]),ship[14]], ship[15])
            fleet_list.append(ship[0])
    return fleet_list

def start_up(fleet):
    fleet_list = []
    for ship in fleet:
        for vessel_class in fleet_list:
            if ship in vessel_class:
                vessel_class[1] += 1
        else:
            fleet_list.append([ship,1])
    return fleet_list

fleet1 = fleet_loader('fleet1.txt')
fleet2 = fleet_loader('fleet1.txt')