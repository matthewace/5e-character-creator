"""Module for all base types of Equipment.

https://www.dndbeyond.com/sources/basic-rules/equipment
https://www.5esrd.com/equipment/

Base Types:
    Adventuring Gear
    Armor and Shields
    Weapons
    Equipment Packs
    Tools
    Mounts and Vehicles
    Trade Goods
    Trinkets
"""
from typing import Dict, List


class Equipment:
    """Base class for sub-classing"""
    name = str
    base_type = str
    item_type = str
    base_cost = str
    base_weight = int
    equipable = bool
    
    def __init__(self):
        self.cost = self.base_cost
        self.weight = self.base_weight

    def __str__(self):
        return f'Name:      {self.name}\n' +\
               f'Base Type: {self.base_type}\n' +\
               f'Item Type: {self.item_type}\n' +\
               f'Cost:      {self.cost}\n' +\
               f'Weight:    {self.weight}\n'


class AdventuringGear(Equipment):
    name = 'Advenguring Gear'
    base_type = 'Adventuring Gear'
    equipable = False


class Armor(Equipment):
    name = 'Armor'
    base_type = 'Armor'
    armor_class = int
    mod_max = int
    min_str = int
    stealth_disadv = bool
    equipable = True


class Weapon(Equipment):
    name = 'Weapon'
    base_type = 'Weapon'
    ranged = bool
    damage_die = str
    damage_type = str
    properties = List[str]
    equipable = True

    def __str__(self):
        return f'{super().__str__()}' +\
               f'Ranged:    {self.ranged}\n' +\
               f'Dmg Die:   {self.damage_die}\n' +\
               f'Dmg Type:  {self.damage_type}\n' +\
               f'Property:  {", ".join(self.properties)}\n'


class EquipmentPack(Equipment):
    name = 'Equipment Pack'
    base_type = 'Equipment Pack'
    item_type = 'Equipment Pack'
    base_contents = Dict[AdventuringGear, int]
    equipable = False

    def __init__(self):
        self.cost = self.base_cost
        self.contents = self.base_contents
        self.weight = self._weight()

    def __str__(self):
        return super().__str__() + 'Contents:\n--------\n' + self._contents()
    
    def _weight(self) -> float:
        """Add up weight of all items in contents"""
        weight = 0
        for item, num in self.contents.items():
            weight += num * item.base_weight
        return weight

    def _contents(self) -> str:
        """Return contents in String format"""
        out = ''
        for item, num in self.contents.items():
            out += f'{num}x\t{item.name}\n'
        return out


class Tool(Equipment):
    name = 'Tool'
    base_type = 'Tool'
    equipable = False


class Mount(Equipment):
    name = 'Mount'
    base_type = 'Mount'
    item_type = 'Mount'
    base_speed = int
    base_carrying_capacity = int
    equipable = False

    def __init__(self):
        super().__init__()
        self.speed = self.base_speed
        self.capacity = self.base_carrying_capacity

    def __str__(self):
        return f'Name:      {self.name}\n' +\
               f'Base Type: {self.base_type}\n' +\
               f'Item Type: {self.item_type}\n' +\
               f'Cost:      {self.cost}\n' +\
               f'Speed:     {self.speed}\n' +\
               f'Carry Cap: {self.capacity}\n'


class TradeGood(Equipment):
    name = 'Trade Good'
    base_type = 'Trade Good'
    equipable = False


class Trinket(Equipment):
    name = 'Trinket'
    base_type = 'Trinket'
    equipable = True


class Vehicle(Equipment):
    name = 'Vehicle'
    base_type = 'Vehicle'
    equipable = False