"""Module for Holy Symbol item tyes

    Amulet, Emblem, Reliquary
"""

from dnd.equipment.base_equipment import AdventuringGear


class HolySymbol(AdventuringGear):
    item_type = 'Holy Symbol'


class Amulet(HolySymbol):
    name = 'Amulet'
    base_cost = '5 gp'
    base_weight = 1


class Emblem(HolySymbol):
    name = 'Emblem'
    base_cost = '5 gp'
    base_weight = 0


class Reliquary(HolySymbol):
    name = 'Reliquary'
    base_cost = '5 gp'
    base_weight = 2