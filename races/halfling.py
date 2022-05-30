from .alignments import LawfulGood, NeutralGood, ChaoticGood
from .baserace import CharacterRace
from .languages import Common, Halfling as HalflingLang
from .sizes import Small


class Halfling(CharacterRace):
    name = "Halfling"
    base_speed = 25
    base_height = 31
    height_mod = '2d4'
    base_weight = 35
    weight_mod = '1d1'
    size = Small
    languages = [
        Common,
        HalflingLang
    ]
    alignments = [
        LawfulGood,
        NeutralGood,
        ChaoticGood
    ]
    male_names = [
        'Alton', 'Ander', 'Cade', 'Corrin', 'Eldon', 'Errich', 'Finnan',
        'Garret', 'Lindal', 'Lyle', 'Merric', 'Milo', 'Osborn', 'Perrin',
        'Reed', 'Roscoe', 'Wellby'
    ]
    female_names = [
        'Andry', 'Bree', 'Callie', 'Cora', 'Euphemia', 'Jillian', 'Kithri',
        'Lavinia', 'Lidda', 'Merla', 'Nedda', 'Paela', 'Portia', 'Seraphina',
        'Shaena', 'Trym', 'Vani', 'Verna'
    ]
    clan_names = [
        'Brushgather', 'Goodbarrel', 'Greenbottle', 'High-hill', 'Hilltopple',
        'Leagallow', 'Tealeaf', 'Thorngage', 'Tosscobble', 'Underbough'
    ]
    traits = [
        ('add_base_ability_points', {
            'ability': 'DEX',
            'points': 2
        }),
        ('add_traits', {
            'traits': ['Lucky', 'Brave', 'Halfling Nimbleness']
        }),
        ('add_languages', {
            'languages': languages
        }),
    ]


class Lightfoot(Halfling):
    """Subrace of Halfling"""
    name = 'Lightfoot Halfling'
    traits = [
        ('add_base_ability_points', {
            'ability': 'CHA',
            'points': 1
        }),
        ('add_traits', {
            'traits': ['Naturally Stealthy']
        }),
    ] + Halfling.traits


class Stout(Halfling):
    """Subrace of Halfling"""
    name = 'Stout Halfling'
    traits = [
        ('add_base_ability_points', {
            'ability': 'CON',
            'points': 1
        }),
        ('add_traits', {
            'traits': ['Stout Resilience']
        }),
    ] + Halfling.traits