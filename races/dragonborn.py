from .alignments import *
from .baserace import CharacterRace
from .languages import Common, Draconic
from .sizes import Medium


class Dragonborn(CharacterRace):
    name = "Dragonborn"
    base_speed = 30
    base_height = 66
    height_mod = '2d8'
    base_weight = 175
    weight_mod = '2d6'
    size = Medium
    languages = [
        Common,
        Draconic,
    ]
    alignments = [
        LawfulGood,
        NeutralGood,
        ChaoticGood,
        LawfulEvil,
        NeutralEvil,
        ChaoticEvil,
    ]
    male_names = [
        'Arjhan', 'Balasar', 'Bharash', 'Donaar', 'Ghesh', 'Heskan', 'Kriv',
        'Medrash', 'Mehen', 'Nadarr', 'Pandjed', 'Patrin', 'Rhogar', 'Shamash',
        'Shedinn', 'Tarhun', 'Torinn'
    ]
    female_names = [
        'Akra', 'Biri', 'Daar', 'Farideh', 'Harann', 'Havilar', 'Jheri',
        'Kava', 'Korinn', 'Mishann', 'Nala', 'Perra', 'Raiann', 'Sora',
        'Surina', 'Thava', 'Uadjit'
    ]
    clan_names = [
        'Clethtinthiallor', 'Daardendrian', 'Delmirev', 'Drachedandion',
        'Fenkenkabradon', 'Kepeshkmolik', 'Kerrhylon', 'Kimbatuul',
        'Linxakasendalor', 'Myastan', 'Nemmonis', 'Norixius',
        'Ophinshtalajiir', 'Prexijandilin', 'Shestendeliath', 'Turnuroth',
        'Verthisathurgiesh', 'Yarjerit'
    ]
    traits = [
        ('add_base_ability_points', {
            'ability': 'STR',
            'points': 2
        }),
        ('add_base_ability_points', {
            'ability': 'CHA',
            'points': 1
        }),
        ('add_languages', {
            'languages': languages
        }),
        ('add_traits', {
            'traits': ['Draonic Ancestry', 'Breath Weapon', 'Damage Resistance']
        }),
    ]