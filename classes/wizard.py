from .characterclass import CharacterClass
from dnd.equipment import *
from dnd.skills import *


class Wizard(CharacterClass):
    name = "Wizard"
    hit_die = '1d6'
    armor_proficiencies = []
    weapon_proficiencies = [
        weapon.Dagger, weapon.Dart, weapon.Quarterstaff, weapon.LightCrossbow
    ]
    tool_proficiencies = []
    saving_throws = ['INT', 'WIS']
    skills = [Arcana, History, Insight, Investigation, Medicine, Religion]
    level = [
        [   #Level 0
            ('add_proficiencies', {
                'items': [
                armor_proficiencies, tool_proficiencies, weapon_proficiencies]
            }),
            ('add_equipment', {
                'items': gear.Spellbook
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [weapon.Quarterstaff, weapon.Dagger]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    gear.ComponentPouch, gear.Crystal, gear.Orb, gear.Rod,
                    gear.Staff, gear.Wand]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [pack.ScholarsPack, pack.ExplorersPack]
            }),
            ('choose_skills', {
                'num': 2,
                'options': skills
            }),
        ],
        [   #Level 1
            ('add_feats', {'feats': ['Spellcasting', 'Arcane Recovery']}),
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