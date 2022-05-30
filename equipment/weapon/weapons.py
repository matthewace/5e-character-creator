"""Module for all standard weapons in DnD 5e.

Weapons are either Simple or Martial, and Melee or Ranged.

Simple-Melee:
    Club, Dagger, GreatClub, HandAxe, Javelin, LightHammer, Mace, Quarterstaff,
    Sickle, Spear

Simple-Ranged:
    LightCrossbow, Dart, Shortbow, Sling

Martial-Melee:
    Battleaxe, Flail, Glaive, Greatsword, Halberd, Lance, Longsword, Maul,
    Morningstar, Pike, Rapier, Scimitar, Shortsword, Trident, Warpick, 
    Warhammer, Whip

Martial-Ranged:
    Blowgun, HandCrossbow, HeavyCrossbow, Longbow, Net
"""
from typing import List

from dnd.equipment.base_equipment import Weapon

"""
class Weapon:
    
    name = str
    ranged = bool
    base_cost = str
    damage_die = str
    damage_type = str
    base_weight = float
    properties = List[str]

    def __init__(self):
        pass
"""


class SimpleWeapon(Weapon):
    """Sub-class to track weapon proficiency"""
    name = 'Simple Weapon'
    item_type = 'Simple Weapon'


class MartialWeapon(Weapon):
    """Sub-class to track weapon proficiency"""
    name = 'Martial Weapon'
    item_type = 'Martial Weapon'


class MeleeWeapon(Weapon):
    ranged = False


class RangedWeapon(Weapon):
    ranged = True


class Club(SimpleWeapon, MeleeWeapon):
    name = 'Club'
    base_cost = '1 Sp'
    damage_die = '1d4'
    damage_type = 'Bludgeoning'
    base_weight = 2
    properties = ['Light']


class Dagger(SimpleWeapon, MeleeWeapon):
    name = 'Dagger'
    base_cost = '2 Gp'
    damage_die = '1d4'
    damage_type = 'Piercing'
    base_weight = 1
    properties = ['Finesse', 'Light', 'Thrown(20, 60)']


class GreatClub(SimpleWeapon, MeleeWeapon):
    name = 'Great-Club'
    base_cost = '2 Sp'
    damage_die = '1d8'
    damage_type = 'Bludgeoning'
    base_weight = 10
    properties = ['Two-Handed']


class HandAxe(SimpleWeapon, MeleeWeapon):
    name = 'Hand-Axe'
    base_cost = '5 Gp'
    damage_die = '1d6'
    damage_type = 'Slashing'
    base_weight = 2
    properties = ['Light', 'Thrown(20, 60)']


class Javelin(SimpleWeapon, MeleeWeapon):
    name = 'Javelin'
    base_cost = '5 Sp'
    damage_die = '1d6'
    damage_type = 'Piercing'
    base_weight = 2
    properties = ['Thrown(30, 120)']


class LightHammer(SimpleWeapon, MeleeWeapon):
    name = 'Light Hammer'
    base_cost = '2 Gp'
    damage_die = '1d4'
    damage_type = 'Bludgeoning'
    base_weight = 2
    properties = ['Light', 'Thrown(20, 60)']


class Mace(SimpleWeapon, MeleeWeapon):
    name = 'Mace'
    base_cost = '5 Gp'
    damage_die = '1d6'
    damage_type = 'Bludgeoning'
    base_weight = 4
    properties = []


class Quarterstaff(SimpleWeapon, MeleeWeapon):
    name = 'Quarterstaff'
    base_cost = '2 Sp'
    damage_die = '1d6'
    damage_type = 'Bludgeoning'
    base_weight = 4
    properties = ['Versatile(1d8)']


class Sickle(SimpleWeapon, MeleeWeapon):
    name = 'Sickle'
    base_cost = '1 Gp'
    damage_die = '1d4'
    damage_type = 'Slashing'
    base_weight = 2
    properties = ['Light']


class Spear(SimpleWeapon, MeleeWeapon):
    name = 'Spear'
    base_cost = '1 Gp'
    damage_die = '1d6'
    damage_type = 'Piercing'
    base_weight = 3
    properties = ['Thrown(20, 60)', 'Versatile(1d8)']


class LightCrossbow(SimpleWeapon, RangedWeapon):
    name = 'Crossbow (Light)'
    base_cost = '25 Gp'
    damage_die = '1d8'
    damage_type = 'Piercing'
    base_weight = 5
    properties = ['Ammunition', 'Range(80, 320)', 'Loading', 'Two-Handed']


class Dart(SimpleWeapon, RangedWeapon):
    name = 'Dart'
    base_cost = '5 Cp'
    damage_die = '1d4'
    damage_type = 'Piercing'
    base_weight = 0.25
    properties = ['Finesse', 'Thrown(20, 60)']


class Shortbow(SimpleWeapon, RangedWeapon):
    name = 'Shortbow'
    base_cost = '25 Gp'
    damage_die = '1d6'
    damage_type = 'Piercing'
    base_weight = 2
    properties = ['Ammunition', 'Range(30, 120)']


class Sling(SimpleWeapon, RangedWeapon):
    name = 'Sling'
    base_cost = '1 Sp'
    damage_die = '1d4'
    damage_type = 'Piercing'
    base_weight = 0
    properties = ['Ammunition', 'Range(30, 120)']


class Battleaxe(MartialWeapon, MeleeWeapon):
    name = 'Battleaxe'
    base_cost = '10 Gp'
    damage_die = '1d8'
    damage_type = 'Slashing'
    base_weight = 4
    properties = ['Versatile(1d10)']


class Flail(MartialWeapon, MeleeWeapon):
    name = 'Flail'
    base_cost = '10 Gp'
    damage_die = '1d8'
    damage_type = 'Bludgeoning'
    base_weight = 2
    properties = []


class Glaive(MartialWeapon, MeleeWeapon):
    name = 'Glaive'
    base_cost = '20 Gp'
    damage_die = '1d10'
    damage_type = 'Slashing'
    base_weight = 6
    properties = ['Heavy', 'Reach', 'Two-Handed']


class Greataxe(MartialWeapon, MeleeWeapon):
    name = 'Greataxe'
    base_cost = '30 gp'
    damage_die = '1d12'
    damage_type = 'Slashing'
    base_weight = 7
    properties = ['Heavy', 'Two-Handed']


class Greatsword(MartialWeapon, MeleeWeapon):
    name = 'Greatsword'
    base_cost = '50 Gp'
    damage_die = '2d6'
    damage_type = 'Slashing'
    base_weight = 6
    properties = ['Heavy', 'Two-Handed']


class Halberd(MartialWeapon, MeleeWeapon):
    name = 'Halberd'
    base_cost = '20 Gp'
    damage_die = '1d10'
    damage_type = 'Slashing'
    base_weight = 6
    properties = ['Heavy', 'Reach', 'Two-Handed']


class Lance(MartialWeapon, MeleeWeapon):
    name = 'Lance'
    base_cost = '10 Gp'
    damage_die = '1d12'
    damage_type = 'Piercing'
    base_weight = 6
    properties = ['Reach', 'Special']


class Longsword(MartialWeapon, MeleeWeapon):
    name = 'Longsword'
    base_cost = '15 Gp'
    damage_die = '1d8'
    damage_type = 'Slashing'
    base_weight = 3
    properties = ['Versatile(1d10)']


class Maul(MartialWeapon, MeleeWeapon):
    name = 'Maul'
    base_cost = '10 Gp'
    damage_die = '2d6'
    damage_type = 'Bludgeoning'
    base_weight = 10
    properties = ['Heavy', 'Two-Handed']


class Morningstar(MartialWeapon, MeleeWeapon):
    name = 'Morningstar'
    base_cost = '15 Gp'
    damage_die = '1d8'
    damage_type = 'Piercing'
    base_weight = 4
    properties = []


class Pike(MartialWeapon, MeleeWeapon):
    name = 'Pike'
    base_cost = '5 Gp'
    damage_die = '1d10'
    damage_type = 'Piercing'
    base_weight = 18
    properties = ['Heavy', 'Reach', 'Two-Handed']


class Rapier(MartialWeapon, MeleeWeapon):
    name = 'Rapier'
    base_cost = '25 Gp'
    damage_die = '1d8'
    damage_type = 'Piercing'
    base_weight = 2
    properties = ['Finesse']


class Scimitar(MartialWeapon, MeleeWeapon):
    name = 'Scimitar'
    base_cost = '25 Gp'
    damage_die = '1d6'
    damage_type = 'Slashing'
    base_weight = 3
    properties = ['Finesse', 'Light']


class Shortsword(MartialWeapon, MeleeWeapon):
    name = 'Shortsword'
    base_cost = '10 Gp'
    damage_die = '1d6'
    damage_type = 'Piercing'
    base_weight = 2
    properties = ['Finesse', 'Light']


class Trident(MartialWeapon, MeleeWeapon):
    name = 'Trident'
    base_cost = '5 Gp'
    damage_die = '1d6'
    damage_type = 'Piercing'
    base_weight = 4
    properties = ['Thrown(20, 60)', 'Versatile(1d8)']


class Warpick(MartialWeapon, MeleeWeapon):
    name = 'War Pick'
    base_cost = '5 Gp'
    damage_die = '1d8'
    damage_type = 'Piercing'
    base_weight = 2
    properties = []


class Warhammer(MartialWeapon, MeleeWeapon):
    name = 'War Hammer'
    base_cost = '15 Gp'
    damage_die = '1d8'
    damage_type = 'Bludgeoning'
    base_weight = 2
    properties = ['Versatile(1d10)']


class Whip(MartialWeapon, MeleeWeapon):
    name = 'Whip'
    base_cost = '2 Gp'
    damage_die = '1d4'
    damage_type = 'Slashing'
    base_weight = 3
    properties = ['Finesse', 'Reach']


class Blowgun(MartialWeapon, RangedWeapon):
    name = 'Blowgun'
    base_cost = '10 Gp'
    damage_die = '1d1'
    damage_type = 'Piercing'
    base_weight = 1
    properties = ['Ammunition', 'Range(25, 100)', 'Loading']


class HandCrossbow(MartialWeapon, RangedWeapon):
    name = 'Crossbow (Hand)'
    base_cost = '75 Gp'
    damage_die = '1d6'
    damage_type = 'Piercing'
    base_weight = 3
    properties = ['Ammunition', 'Range(30, 120)', 'Light', 'Loading']


class HeavyCrossbow(MartialWeapon, RangedWeapon):
    name = 'Crossbow (Heavy)'
    base_cost = '50 Gp'
    damage_die = '1d10'
    damage_type = 'Piercing'
    base_weight = 18
    properties = ['Ammunition', 'Range(100, 400)', 'Heavy', 'Loading',
                  'Two-Handed']


class Longbow(MartialWeapon, RangedWeapon):
    name = 'Longbow'
    base_cost = '50 Gp'
    damage_die = '1d8'
    damage_type = 'Piercing'
    base_weight = 12
    properties = ['Ammunition', 'Range(150, 600)', 'Heavy', 'Two-Handed']


class Net(MartialWeapon, RangedWeapon):
    name = 'Net'
    base_cost = '1 Gp'
    damage_die = '0d1'
    damage_type = ''
    base_weight = 3
    properties = ['Special', 'Thrown(5, 15)']