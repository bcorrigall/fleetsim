            if ship2 != None and len(fleet1) != 0 and ship2.tonnage > 0 and ship.status == 'functional': 
                for ship in fleet1_zone_dict:
                    if abs(fleet1_zone_dict[ship] - fleet2_zone_dict[ship2]) > 3 + ship2.weaponry[2] or ship.status != 'functional':
                        ship2_move_counter = True
                    else:
                        ship2_move_counter = False
                        break
                if ship2_move_counter == True:
                    fleet2_zone_dict[ship2] -= (1 + ship2.thrusters//3)
                    print(f'{ship2.name} advances on the enemy.')