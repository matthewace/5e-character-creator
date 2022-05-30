"""Module for Vehciles

    Land: Carriage, Cart, Chariot, Sled, Wagon
    Waterborne: Galley, Keelboat, Longship, Rowboat, Sailingship, Warship
"""

from dnd.equipment.base_equipment import Vehicle


class LandVehicle(Vehicle):
    item_type = 'Vehicle (Land)'


class WaterborneVehicle(Vehicle):
    item_type = 'Vehicle (Waterborne)'
    base_speed = float

    def __init__(self):
        super().__init__()
        self.speed = self.base_speed

    def __str__(self):
        return f'Name:      {self.name}\n' +\
               f'Base Type: {self.base_type}\n' +\
               f'Item Type: {self.item_type}\n' +\
               f'Cost:      {self.cost}\n' +\
               f'Speed:     {self.speed} mph\n'


class Carriage(LandVehicle):
    name = 'Carriage'
    base_cost = '100 gp'
    base_weight = 600


class Cart(LandVehicle):
    name = 'Cart'
    base_cost = '15 gp'
    base_weight = 200
    
    
class Chariot(LandVehicle):
    name = 'Chariot'
    base_cost = '250 gp'
    base_weight = 100

    
class Sled(LandVehicle):
    name = 'Sled'
    base_cost = '20 gp'
    base_weight = 100
    
    
class Wagon(LandVehicle):
    name = 'Wagon'
    base_cost = '35 gp'
    base_weight = 400


class Galley(WaterborneVehicle):
    name = 'Galley'
    base_cost = '30000 gp'
    base_speed = 4
    

class Keelboat(WaterborneVehicle):
    name = 'Keelboat'
    base_cost = '3000 gp'
    base_speed = 1
    
    
class Longship(WaterborneVehicle):
    name = 'Longship'
    base_cost = '10000 gp'
    base_speed = 3
    
    
class Rowboat(WaterborneVehicle):
    name = 'Rowboat'
    base_cost = '50 gp'
    base_speed = 1.5
    
    
class Sailingship(WaterborneVehicle):
    name = 'Sailing Ship'
    base_cost = '10000 gp'
    base_speed = 2
    
    
class Warship(WaterborneVehicle):
    name = 'Warship'
    base_cost = '25000 gp'
    base_speed = 2.5