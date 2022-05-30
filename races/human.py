from .alignments import *
from .baserace import CharacterRace
from .languages import *
from .sizes import Medium


class Human(CharacterRace):
    name = "Human"
    base_speed = 30
    base_height = 56
    height_mod = '2d10'
    base_weight = 110
    weight_mod = '2d4'
    size = Medium
    languages = [
        Common
    ]
    alignments = [
        LawfulGood,
        NeutralGood,
        ChaoticGood,
        NeutralGood,
        TrueNeutral,
        NeutralEvil,
        ChaoticGood,
        ChaoticNeutral,
        ChaoticEvil
    ]
    male_names = [
        'Ander', 'Blath', 'Bran', 'Frath', 'Geth', 'Lander', 'Luth', 'Malcer',
        'Stor', 'Taman', 'Urth', 'An', 'Chen', 'Chi', 'Fai', 'Jiang', 'Jun',
        'Lian', 'Long', 'Meng', 'On', 'Shan', 'Shui', 'Wen', 'Anton', 'Diero',
        'Marcon', 'Pieron', 'Rimardo', 'Romero', 'Salazar', 'Umbero'
    ]
    female_names = [
        'Balama', 'Dona', 'Faila', 'Jalana', 'Luisa', 'Marta', 'Quara',
        'Selise', 'Vonda', 'Bai', 'Chao', 'Jia', 'Lei', 'Mei', 'Qiao', 'Shui',
        'Tai', 'Arveene', 'Esvele', 'Jhessail', 'Kerri', 'Lureene', 'Miri',
        'Rowan', 'Shandri', 'Tessele'
    ]
    clan_names = [
        'Amblecrown', 'Buckman', 'Dundragon', 'Evenwood', 'Greycastle',
        'Tallstag', 'Brightwood', 'Helder', 'Hornraven', 'Lackman',
        'Stormwind', 'Windrivver', 'Chien', 'Huang', 'Kao', 'Kung', 'Lao',
        'Ling', 'Mei', 'Pin', 'Shin', 'Sum', 'Tan', 'Wan', 'Agosto', 'Astorio',
        'Calabra', 'Domine', 'Falone', 'Marivaldi', 'Pisacar', 'Ramondo'
    ]
    traits = [
        ('add_base_ability_points', {
            'ability': 'STR',
            'points': 1
        }),
        ('add_base_ability_points', {
            'ability': 'DEX',
            'points': 1
        }),
        ('add_base_ability_points', {
            'ability': 'CON',
            'points': 1
        }),
        ('add_base_ability_points', {
            'ability': 'INT',
            'points': 1
        }),
        ('add_base_ability_points', {
            'ability': 'WIS',
            'points': 1
        }),
        ('add_base_ability_points', {
            'ability': 'CHA',
            'points': 1
        }),
        ('add_languages', {
            'languages': languages
        }),
        ('choose_language', {
            'num': 1, 
            'options': [
                Abyssal, Celestial, DeepSpeech, Draconic, Dwarvish, Giant,
                Gnomish, Goblin, Halfling, Infernal, Orcish, Primordial,
                Sylvan, Undercommon]
        }),
    ]