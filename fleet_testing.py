# testing for fleet battles

from fleet import Ship
from fleet import fleet_combat
from fleet import fleet_loader
from fleet import start_up
import random

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

fleet1 = fleet_loader('tyranid_fleet.txt')
fleet2 = fleet_loader('imperial_fleet.txt')

def start_up(fleet):
    fleet_dict = {}
    for ship in fleet:
        if ship.model in fleet_dict:
            fleet_dict[ship.model] += 1
        else:
            fleet_dict[ship.model] = 1
    return fleet_dict

fleet1_vessels = start_up(fleet1)
fleet2_vessels = start_up(fleet2)

print('Fleet one contains: ',end=' ')
for ship in fleet1_vessels:
    if fleet1_vessels[ship] == 1:
        print(f'{fleet1_vessels[ship]} {ship}',end=' ')
    else:
        print(f'{fleet1_vessels[ship]} {ship}s',end=' ')
print('\n')
print('Fleet two contains: ',end=' ')
for ship in fleet2_vessels:
    if fleet2_vessels[ship] == 1:
        print(f'{fleet2_vessels[ship]} {ship}',end=' ')
    else:
        print(f'{fleet2_vessels[ship]} {ship}s',end=' ')
print('\n')

fleet1, fleet2 = fleet_combat(fleet1, fleet2)

for ship in fleet1:
    print(ship.model,end=' ')
print()
for ship in fleet2:
    print(ship.model,end=' ')
print()