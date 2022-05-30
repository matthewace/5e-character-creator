from .alignments import ChaoticEvil, ChaoticNeutral
from .baserace import CharacterRace
from .languages import Common, Orcish
from .sizes import Medium
from dnd.skills import Intimidation


class HalfOrc(CharacterRace):
    name = "Half-Orc"
    base_speed = 30
    base_height = 58
    height_mod = '2d10'
    base_weight = 140
    weight_mod = '2d6'
    size = Medium
    languages = [
        Common,
        Orcish
    ]
    alignments = [
        ChaoticEvil,
        ChaoticNeutral
    ]
    male_names = [
        'Dench', 'Feng', 'Gell', 'Henk', 'Holg', 'Imsh', 'Keth', 'Krusk',
        'Mhurren', 'Ront', 'Shump', 'Thokk'
    ]
    female_names = [
        'Baggi', 'Emen', 'Engong', 'Kansif', 'Myev', 'Neega', 'Ovak', 'Ownka',
        'Shautha', 'Sutha', 'Vola', 'Volen', 'Yevelda'
    ]
    clan_names = ['']
    traits = [
        ('add_base_ability_points', {
            'ability': 'STR',
            'points': 2
        }),
        ('add_base_ability_points', {
            'ability': 'CON',
            'points': 1
        }),
        ('add_languages', {
            'languages': languages
        }),
        ('add_skills', {
            'skills': [Intimidation]
        }),
        ('add_traits', {
            'traits': [
                'Darkvision', 'Menacing', 'Restless Endurance',
                'Savage Attacks']
        }),
    ]