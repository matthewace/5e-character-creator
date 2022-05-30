from .characterclass import CharacterClass
from dnd.equipment import *
from dnd.skills import *


class Bard(CharacterClass):
    name = "Bard"
    hit_die = '1d8'
    armor_proficiencies = [armor.LightArmor]
    tool_proficiencies = []
    weapon_proficiencies = [
        weapon.SimpleWeapon, weapon.HandCrossbow, weapon.Longsword,
        weapon.Rapier, weapon.Shortsword
    ]
    saving_throws = ['DEX', 'CHA']
    skills = [
        Acrobatics, AnimalHandling, Arcana, Athletics, Deception, History,
        Insight, Intimidation, Investigation, Medicine, Nature, Perception,
        Performance, Persuasion, Religion, SleightOfHand, Stealth, Survival
    ]
    level = [
        [   #Level 0
            ('add_proficiencies', {
                'items': [
                armor_proficiencies, tool_proficiencies, weapon_proficiencies]
            }),
            ('add_equipment', {
                'items': [armor.Leather, weapon.Dagger]
            }),
            ('choose_proficiencies', {
                'num': 3,
                'options': [
                    tool.Bagpipes, tool.Drum, tool.Dulcimer, tool.Flute,
                    tool.Lute, tool.Horn, tool.PanFlute, tool.Shawm, tool.Viol]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    tool.Bagpipes, tool.Drum, tool.Dulcimer, tool.Flute,
                    tool.Lute, tool.Horn, tool.PanFlute, tool.Shawm, tool.Viol]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [pack.DiplomatsPack, pack.EntertainersPack]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    weapon.Rapier, weapon.Longsword, weapon.Club,
                    weapon.Dagger, weapon.GreatClub, weapon.HandAxe,
                    weapon.Javelin, weapon.LightHammer, weapon.Mace,
                    weapon.Quarterstaff, weapon.Sickle, weapon.Spear,
                    weapon.LightCrossbow, weapon.Dart, weapon.Shortbow,
                    weapon.Sling]
            }),
            ('choose_skills', {
                'num': 3,
                'options': skills
            }),
        ],
        [   #Level 1
            ('add_feats', {'feats': ['Spellcasting', 'BardicInspiration']}),
        ],
        [   #Level 2

        ],
        [   #Level 3

        ],
        [   #Level 4

        ],
        [   #Level 5

        ],
        [   #Level 6

        ],
        [   #Level 7

        ],
        [   #Level 8

        ],
        [   #Level 9

        ],
        [   #Level 10

        ],
        [   #Level 11

        ],
        [   #Level 12

        ],
        [   #Level 13

        ],
        [   #Level 14

        ],
        [   #Level 15

        ],
        [   #Level 16

        ],
        [   #Level 17

        ],
        [   #Level 18

        ],
        [   #Level 19

        ],
        [   #Level 20

        ],
    ]