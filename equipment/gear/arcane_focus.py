"""Module for Arcane Focus items.

    Crystal, Orb, Rod, Staff, Wand
"""

from dnd.equipment.base_equipment import AdventuringGear


class ArcaneFocus(AdventuringGear):
    item_type = 'Arcane Focus'


class Crystal(ArcaneFocus):
    name = 'Crystal'
    base_cost = '10 gp'
    base_weight = 1


class Orb(ArcaneFocus):
    name = 'Orb'
    base_cost = '20 gp'
    base_weight = 3


class Rod(ArcaneFocus):
    name = 'Rod'
    base_cost = '10 gp'
    base_weight = 2


class Staff(ArcaneFocus):
    name = 'Staff'
    base_cost = '5 gp'
    base_weight = 4


class Wand(ArcaneFocus):
    name = 'Wand'
    base_cost = '10 gp'
    base_weight = 1