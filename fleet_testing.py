# testing for fleet battles

from fleet import Ship
from fleet import fleet_combat
from fleet import fleet_loader
from fleet import start_up
from fleet import combat_grid
import random

fleet1 = fleet_loader('fleet1.txt')
fleet2 = fleet_loader('fleet2.txt')

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
    if ship.status == 'functional':
        print(ship.model,end=' ')
print()
for ship in fleet2:
    if ship.status == 'functional':
        print(ship.model,end=' ')
print()