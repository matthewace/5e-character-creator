from .alignments import LawfulGood, LawfulNeutral, LawfulEvil
from .baserace import CharacterRace
from .languages import Common, Dwarvish
from .sizes import Medium
from dnd.equipment.tool import SmithsTools, BrewersSupplies, MasonsTools
from dnd.equipment.weapon import Battleaxe, HandAxe, LightHammer, Warhammer


class Dwarf(CharacterRace):
    name = "Dwarf"
    base_speed = 25
    base_height = 48
    height_mod = '2d4'
    base_weight = 130
    weight_mod = '2d6'
    size = Medium
    languages = [
        Common,
        Dwarvish
    ]
    alignments = [
        LawfulGood,
        LawfulNeutral,
        LawfulEvil
    ]
    male_names = [
        'Adrik', 'Alberich', 'Baern', 'Barendd', 'Brottor', 'Bruenor', 'Dain',
        'Darrak', 'Delg', 'Eberk', 'Einkil', 'Fargrim', 'Flint', 'Gardain',
        'Harbek', 'Kildrak', 'Morgran', 'Orsik', 'Oskar', 'Rangrim', 'Rurik',
        'Taklinn', 'Thoradin', 'Thorin', 'Tordek', 'Traubon', 'Travok',
        'Ulfgar', 'Veit', 'Vondal'
    ]
    female_names = [
        'Amber', 'Artin', 'Audhild', 'Bardryn', 'Dagnal', 'Diesa', 'Eldeth',
        'Falkrunn', 'Finellen', 'Gunnloda', 'Gurdis', 'Helja', 'Hlin',
        'Kathra', 'Kristryd', 'Ilde', 'Liftrasa', 'Mardred', 'Riswynn',
        'Sannl', 'Torbera', 'Torgga', 'Vistra'
    ]
    clan_names = [
        'Balderk', 'Battlehammer', 'Brawnanvil', 'Dankil', 'Fireforge',
        'Frostbeard', 'Gorunn', 'Holderhek', 'Ironfist', 'Loderr', 'Lutgehr',
        'Rumnaheim', 'Strakeln', 'Torunn', 'Ungart'
    ]
    traits = [
        ('add_base_ability_points', {
            'ability': 'CON',
            'points': 2
        }),
        ('add_traits', {
            'traits': ['Darkvision', 'Dwarven Resilience', 'Stonecunning']
        }),
        ('add_proficiencies', {
            'items': [Battleaxe, HandAxe, LightHammer, Warhammer]
        }),
        ('add_languages', {
            'languages': languages
        }),
        ('choose_proficiencies', {
            'num': 1,
            'options': [SmithsTools, BrewersSupplies, MasonsTools]
        }),
    ]


class HillDwarf(Dwarf):
    """Sub-Race of Dwarf"""
    name = "Hill Dwarf"
    traits = [
        ('add_base_ability_points', {
            'ability': 'WIS',
            'points': 1
        }),
        ('add_traits', {
            'traits': ['Dwarven Toughness']
        }),
    ] + Dwarf.traits


class MountainDwarf(Dwarf):
    """Sub-Race of Dwarf"""
    name = "Mountain Dwarf"
    traits = [
        ('add_base_ability_points', {
            'ability': 'STR',
            'points': 2
        }),
        ('add_proficiencies', {
            'items': ['Light', 'Medium']
        }),
    ] + Dwarf.traits