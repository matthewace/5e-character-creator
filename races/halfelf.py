from .alignments import ChaoticGood, ChaoticNeutral, ChaoticEvil
from .baserace import CharacterRace
from .languages import *
from .sizes import Medium
from dnd.skills import *


class HalfElf(CharacterRace):
    name = "Half-Elf"
    base_speed = 30
    base_height = 57
    height_mod = '2d8'
    base_weight = 110
    weight_mod = '2d4'
    size = Medium
    languages = [
        Common,
        Elvish
    ]
    alignments = [
        ChaoticGood,
        ChaoticNeutral,
        ChaoticEvil
    ]
    male_names = [
        'Adran', 'Aelar', 'Aramil', 'Arannis', 'Aust', 'Beiro', 'Berrian',
        'Carric', 'Enialis', 'Erdan', 'Erevan', 'Galinndan', 'Hadarai',
        'Heian', 'Himo', 'Immeral', 'Ivellios', 'Laucian', 'Mindartis',
        'Paelias', 'Peren', 'Quarion', 'Riardon', 'Rolen', 'Soveliss',
        'Thamior', 'Tharivol', 'Theren', 'Varis', 'Ander', 'Blath', 'Bran',
        'Frath', 'Geth', 'Lander', 'Luth', 'Malcer', 'Stor', 'Taman', 'Urth',
        'An', 'Chen', 'Chi', 'Fai', 'Jiang', 'Jun', 'Lian', 'Long', 'Meng',
        'On', 'Shan', 'Shui', 'Wen', 'Anton', 'Diero', 'Marcon', 'Pieron',
        'Rimardo', 'Romero', 'Salazar', 'Umbero'
    ]
    female_names = [
        'Adrie', 'Althaea', 'Anastrianna', 'Andraste', 'Antinua', 'Bethrynna',
        'Birel', 'Caelynn', 'Drusilia', 'Enna', 'Felosial', 'Ielenia',
        'Jelenneth', 'Keyleth', 'Leshanna', 'Lia', 'Meriele', 'Mialee',
        'Naivara', 'Quelenna', 'Quillathe', 'Sariel', 'Shanairra', 'Shava',
        'Silaqui', 'Theirastra', 'Thia', 'Vadania', 'Valanthe', 'Xanaphia',
        'Balama', 'Dona', 'Faila', 'Jalana', 'Luisa', 'Marta', 'Quara',
        'Selise', 'Vonda', 'Bai', 'Chao', 'Jia', 'Lei', 'Mei', 'Qiao', 'Shui',
        'Tai', 'Arveene', 'Esvele', 'Jhessail', 'Kerri', 'Lureene', 'Miri',
        'Rowan', 'Shandri', 'Tessele'
    ]
    clan_names = [
        'Amakiir', 'Amastacia', 'Galanodel', 'Holimion', 'Ilphelkiir',
        'Liadon', 'Meliamne', 'Naïlo', 'Siannodel', 'Xiloscient',
        'Amblecrown', 'Buckman', 'Dundragon', 'Evenwood', 'Greycastle',
        'Tallstag', 'Brightwood', 'Helder', 'Hornraven', 'Lackman',
        'Stormwind', 'Windrivver', 'Chien', 'Huang', 'Kao', 'Kung', 'Lao',
        'Ling', 'Mei', 'Pin', 'Shin', 'Sum', 'Tan', 'Wan', 'Agosto', 'Astorio',
        'Calabra', 'Domine', 'Falone', 'Marivaldi', 'Pisacar', 'Ramondo'
    ]
    traits = [
        ('add_languages', {
            'languages': languages
        }),
        ('add_base_ability_points', {
            'ability': 'CHA',
            'points': 2
        }),
        ('add_traits', {
            'traits': ['Darkvision', 'Fey Ancestry']
        }),
        ('choose_ability_points', {
            'num': 2,
            'options': ['STR', 'DEX', 'CON', 'INT', 'WIS'],
            'unique': True
        }),
        ('choose_language', {
            'num': 1, 
            'options': [
                Abyssal, Celestial, DeepSpeech, Draconic, Dwarvish, Giant,
                Gnomish, Goblin, Halfling, Infernal, Orcish, Primordial,
                Sylvan, Undercommon]
        }),
        ('choose_skills', {
            'num': 2,
            'options': [
                Acrobatics, AnimalHandling, Arcana, Athletics, Deception,
                History, Insight, Intimidation, Investigation, Medicine,
                Nature, Perception, Performance, Persuasion, Religion,
                SleightOfHand, Stealth, Survival]
        }),
    ]