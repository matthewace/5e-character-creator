from .alignments import LawfulGood, NeutralGood, ChaoticGood
from .baserace import CharacterRace
from .languages import Common, Gnomish
from .sizes import Small


class Gnome(CharacterRace):
    name = "Gnome"
    base_speed = 25
    base_height = 35
    height_mod = '2d4'
    base_weight = 35
    weight_mod = '1d1'
    size = Small
    languages = [
        Common,
        Gnomish
    ]
    alignments = [
        LawfulGood,
        NeutralGood,
        ChaoticGood
    ]
    male_names = [
        'Alston', 'Alvyn', 'Boddynock', 'Brocc', 'Burgell', 'Dimble', 'Eldon',
        'Erky', 'Fonkin', 'Frug', 'Gerbo', 'Gimble', 'Glim', 'Jebeddo',
        'Kellen', 'Namfoodle', 'Orryn', 'Roondar', 'Seebo', 'Sindri', 'Warryn',
        'Wrenn', 'Zook'
    ]
    female_names = [
        'Bimpnottin', 'Breena', 'Caramip', 'Carlin', 'Donella', 'Duvamil',
        'Ella', 'Ellyjobell', 'Ellywick', 'Lilli', 'Loopmottin', 'Lorilla',
        'Mardnab', 'Nissa', 'Nyx', 'Oda', 'Orla', 'Roywyn', 'Shamil', 'Tana',
        'Waywocket', 'Zanna'
    ]
    clan_names = [
        'Beren', 'Daergel', 'Folkor', 'Garrick', 'Nackle', 'Murnig', 'Ningel',
        'Raulnor', 'Scheppen', 'Timbers', 'Turen'
    ]
    traits = [
        ('add_languages', {
            'languages': languages
        }),
        ('add_base_ability_points', {
            'ability': 'INT',
            'points': 2
        }),
        ('add_traits', {
            'traits': ['Darkvision', 'Gnome Cunning']
        }),
    ]


class RockGnome(Gnome):
    """Sub-race of Gnome"""
    name = 'Rock Gnome'
    traits = [
        ('add_base_ability_points', {
            'ability': 'CON',
            'points': 1
        }),
        ('add_traits', {
            'traits': ["Artificer's Lore", 'Tinker']
        }),
    ] + Gnome.traits


class ForestGnome(Gnome):
    """Sub-race of Gnome"""
    name = 'Forest Gnome'
    traits = [
        ('add_base_ability_points', {
            'ability': 'DEX',
            'points': 1
        }),
        ('add_traits', {
            'traits': ['Natural Illusionist', 'Speak with Small Beasts']
        }),
    ] + Gnome.traits