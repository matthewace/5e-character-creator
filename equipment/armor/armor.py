"""Module for all the standard Armor types in DnD 5e.

https://www.dndbeyond.com/sources/basic-rules/equipment#ArmorandShields

Armor has several types which a character can be proficient in:
    LightArmor: 
        Padded, Leather, StuddedLeather

    MediumArmor:
        Hide, ChainShirt, ScaleMail, BreastPlate, HalfPlate

    HeavyArmor:
        RingMail, ChainMail, Splint, Plate

    Shield:
        #TODO: sub-classes for Shield

Unique Parameters:
------------------
armor_class : int
    Determines the base AC of character wearing armor.
dex_mod : int
    Maximum DEX modifier to add to AC
min_str : str
    Minimus STR ability to wear armor effectively.
stealth_disadv : bool
    Character has disadvantage on Stealth(DEX) checks if True.

#TODO: Don and Doff times
"""

from dnd.equipment.base_equipment import Armor


class LightArmor(Armor):
    name = 'Light Armor'
    item_type = 'Light Armor'
    dex_mod = 99
    min_str = 0


class MediumArmor(Armor):
    name = 'Medium Armor'
    item_type = 'Medium Armor'
    dex_mod = 2
    min_str = 0


class HeavyArmor(Armor):
    name = 'Heavy Armor'
    item_type = 'Heavy Armor'
    dex_mod = 0
    stealth_disadv = True


class Shield(Armor):
    name = 'Shield'
    item_type = 'Shield'
    base_cost = '10 gp'
    base_weight = 6
    armor_class = 2
    dex_mod = 0
    min_str = 0
    stealth_disadv = False

    def __init__(self, material: str = 'Wood'):
        super().__init__()
        self.material = material
        self.name = f'{self.material} Shield'


class Padded(LightArmor):
    name = 'Padded Armor'
    base_cost = '5 gp'
    base_weight = 8
    armor_class = 11
    stealth_disadv = True


class Leather(LightArmor):
    name = 'Leather Armor'
    base_cost = '10 gp'
    base_weight = 10
    armor_class = 11
    stealth_disadv = False
    
    
class StuddedLeather(LightArmor):
    name = 'Studded Leather Armor'
    base_cost = '45 gp'
    base_weight = 13
    armor_class = 12
    stealth_disadv = False


class Hide(MediumArmor):
    name = 'Hide Armor'
    base_cost = '10 gp'
    base_weight = 12
    armor_class = 12
    stealth_disadv = False


class ChainShirt(MediumArmor):
    name = 'Chain Shirt Armor'
    base_cost = '50 gp'
    base_weight = 20
    armor_class = 13
    stealth_disadv = False

        
class ScaleMail(MediumArmor):
    name = 'Scale Mail Armor'
    base_cost = '50 gp'
    base_weight = 45
    armor_class = 14
    stealth_disadv = True

        
class BreastPlate(MediumArmor):
    name = 'Breast Plate Armor'
    base_cost = '400 gp'
    base_weight = 20
    armor_class = 14
    stealth_disadv = False

        
class HalfPlate(MediumArmor):
    name = 'Half Plate Armor'
    base_cost = '750 gp'
    base_weight = 40
    armor_class = 15
    stealth_disadv = True


class RingMail(HeavyArmor):
    name = 'Ring Mail Armor'
    base_cost = '30 gp'
    base_weight = 40
    armor_class = 14
    min_str = 0


class ChainMail(HeavyArmor):
    name = 'Chain Mail Armor'
    base_cost = '75 gp'
    base_weight = 55
    armor_class = 16
    min_str = 13

    
class Splint(HeavyArmor):
    name = 'Splint Armor'
    base_cost = '200 gp'
    base_weight = 60
    armor_class = 17
    min_str = 15

    
    
class Plate(HeavyArmor):
    name = 'Plate Armor'
    base_cost = '1500 gp'
    base_weight = 65
    armor_class = 18
    min_str = 15