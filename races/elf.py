from .alignments import ChaoticGood, ChaoticNeutral
from .baserace import CharacterRace
from .languages import *
from .sizes import Medium
from dnd.equipment.weapon import Longbow, Longsword, Shortbow, Shortsword


class Elf(CharacterRace):
    name = "Elf"
    base_speed = 30
    base_height = 54
    height_mod = '2d10'
    base_weight = 90
    weight_mod = '1d4'
    size = Medium
    languages = [
        Common,
        Elvish,
    ]
    alignments = [
        ChaoticGood,
        ChaoticNeutral
    ]
    male_names = [
        'Adran', 'Aelar', 'Aramil', 'Arannis', 'Aust', 'Beiro', 'Berrian',
        'Carric', 'Enialis', 'Erdan', 'Erevan', 'Galinndan', 'Hadarai',
        'Heian', 'Himo', 'Immeral', 'Ivellios', 'Laucian', 'Mindartis',
        'Paelias', 'Peren', 'Quarion', 'Riardon', 'Rolen', 'Soveliss',
        'Thamior', 'Tharivol', 'Theren', 'Varis'
    ]
    female_names = [
        'Adrie', 'Althaea', 'Anastrianna', 'Andraste', 'Antinua', 'Bethrynna',
        'Birel', 'Caelynn', 'Drusilia', 'Enna', 'Felosial', 'Ielenia',
        'Jelenneth', 'Keyleth', 'Leshanna', 'Lia', 'Meriele', 'Mialee',
        'Naivara', 'Quelenna', 'Quillathe', 'Sariel', 'Shanairra', 'Shava',
        'Silaqui', 'Theirastra', 'Thia', 'Vadania', 'Valanthe', 'Xanaphia'
    ]
    clan_names = [
        'Amakiir', 'Amastacia', 'Galanodel', 'Holimion', 'Ilphelkiir',
        'Liadon', 'Meliamne', 'Naïlo', 'Siannodel', 'Xiloscient'
    ]
    traits = [
        ('add_base_ability_points', {
            'ability': 'DEX',
            'points': 2
        }),
        ('add_traits', {
            'traits': ['Darkvision', 'Keen Senses', 'Fey Ancestry', 'Trance']
        }),
        ('add_languages', {
            'languages': languages
        }),
    ]


class HighElf(Elf):
    """Sub-race of Elf"""
    name = "High Elf"
    traits = [
        ('add_base_ability_points', {
            'ability': 'INT',
            'points': 1
        }),
        ('add_proficiencies', {
            'items': [Longbow, Longsword, Shortbow, Shortsword]
        }),
        ('choose_cantrips', {
            'num': 1,
            'options': []
        }),
        ('choose_language', {
            'num': 1,
            'options': [
                Abyssal, Celestial, DeepSpeech, Draconic, Dwarvish, Giant,
                Gnomish, Goblin, Halfling, Infernal, Orcish, Primordial,
                Sylvan, Undercommon]
        }),
    ] + Elf.traits


class WoodElf(Elf):
    """Sub-race of Elf"""
    name = "Wood Elf"
    base_speed = 35 #Fleet of Foot
    traits = [
        ('add_base_ability_points', {
            'ability': 'WIS',
            'points': 1
        }),
        ('add_proficiencies', {
            'items': [Longbow, Longsword, Shortbow, Shortsword]
        }),
        ('add_traits', {
            'traits': ['Fleet of Foot', 'Mask of the Wild']
        }),
    ] + Elf.traits