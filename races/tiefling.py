from .alignments import ChaoticEvil, ChaoticGood, ChaoticNeutral
from .baserace import CharacterRace
from .languages import Common, Infernal
from .sizes import Medium


class Tiefling(CharacterRace):
    name = "Tiefling"
    base_speed = 30
    base_height = 57
    height_mod = '2d8'
    base_weight = 110
    weight_mod = '2d4'
    size = Medium
    languages = [
        Common,
        Infernal
    ]
    alignments = [
        ChaoticEvil,
        ChaoticGood,
        ChaoticNeutral
    ]
    male_names = [
        'Akmenos', 'Amnon', 'Barakas', 'Damakos', 'Ekemon', 'Iados', 'Kairon',
        'Leucis', 'Melech', 'Mordai', 'Morthos', 'Pelaios', 'Skamos', 'Therai'
    ]
    female_names = [
        'Akta', 'Anakis', 'Bryseis', 'Criella', 'Damaia', 'Ea', 'Kallista',
        'Lerissa', 'Makaria', 'Nemeia', 'Orianna', 'Phelaia', 'Rieta'
    ]
    clan_names = [
        'Art', 'Carrion', 'Chant', 'Creed', 'Despair', 'Excellence', 'Fear',
        'Glory', 'Hope', 'Ideal', 'Music', 'Nowhere', 'Open', 'Poetry',
        'Quest', 'Random', 'Reverence', 'Sorrow', 'Temerity', 'Torment',
        'Weary'
    ]
    traits = [
        ('add_base_ability_points', {
            'ability': 'INT',
            'points': 1
        }),
        ('add_base_ability_points', {
            'ability': 'CHA',
            'points': 2
        }),
        ('add_languages', {
            'languages': languages
        }),
        ('add_traits', {
            'traits': ['Darkvision', 'Hellish Resistance', 'Infernal Legacy']
        }),
    ]