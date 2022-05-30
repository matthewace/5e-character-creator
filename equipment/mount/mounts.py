"""Module for Mount type items

    Camel, Donkey, Elephant, DraftHorse, RidingHorse, Mastiff, Pony, WarHorse
"""

from dnd.equipment.base_equipment import Mount


class Camel(Mount):
    name = 'Camel'
    base_cost = '50 gp'
    base_speed = 50
    base_carrying_capacity = 480


class Donkey(Mount):
    name = 'Donkey'
    base_cost = '8 gp'
    base_speed = 40
    base_carrying_capacity = 420


class Mule(Donkey):
    name = 'Mule'


class Elephant(Mount):
    name = 'Elephant'
    base_cost = '200 gp'
    base_speed = 40
    base_carrying_capacity = 1320


class DraftHorse(Mount):
    name = 'Draft Horse'
    base_cost = '50 gp'
    base_speed = 40
    base_carrying_capacity = 540


class Mule(Donkey):
    name = 'Mule'


class RidingHorse(Mount):
    name = 'Riding Horse'
    base_cost = '75 gp'
    base_speed = 60
    base_carrying_capacity = 480


class Mastiff(Mount):
    name = 'Mastiff'
    base_cost = '25 gp'
    base_speed = 40
    base_carrying_capacity = 195


class Pony(Mount):
    name = 'Pony'
    base_cost = '30 gp'
    base_speed = 40
    base_carrying_capacity = 225


class WarHorse(Mount):
    name = 'War Horse'
    base_cost = '400 gp'
    base_speed = 60
    base_carrying_capacity = 540