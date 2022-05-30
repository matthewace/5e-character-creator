"""Module for Druidic Focus items

    SprigOfMistletoe, Totem, WoodenStaff, YewWand
"""

from dnd.equipment.base_equipment import AdventuringGear


class DruidicFocus(AdventuringGear):
    item_type = 'Druidic Focus'


class SprigOfMistletoe(DruidicFocus):
    name = 'Sprig of Mistletoe'
    base_cost = '1 gp'
    base_weight = 0


class Totem(DruidicFocus):
    name = 'Totem'
    base_cost = '1 gp'
    base_weight = 0


class WoodenStaff(DruidicFocus):
    name = 'Wooden Staff'
    base_cost = '5 gp'
    base_weight = 4


class YewWand(DruidicFocus):
    name = 'Yew Wand'
    base_cost = '10 gp'
    base_weight = 1