from .characterclass import CharacterClass
from dnd.equipment import *
from dnd.skills import *


class Ranger(CharacterClass):
    name = "Ranger"
    hit_die = '1d10'
    armor_proficiencies = [armor.LightArmor, armor.MediumArmor, armor.Shield]
    tool_proficiencies = []
    weapon_proficiencies = [weapon.SimpleWeapon, weapon.MartialWeapon]
    saving_throws = ['STR', 'DEX']
    skills = [
        AnimalHandling, Athletics, Insight, Investigation, Nature, Perception,
        Stealth, Survival
    ]
    level = [
        [   #Level 0
            ('add_proficiencies', {
                'items': [
                armor_proficiencies, tool_proficiencies, weapon_proficiencies]
            }),
            ('add_equipment', {
                'items': [weapon.Longbow, gear.Quiver, gear.Arrow]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [armor.ScaleMail, armor.Leather]
            }),
            ('choose_equipment', {
                'num': 2,
                'options': [
                    weapon.Shortsword, weapon.Club, weapon.Dagger,
                    weapon.GreatClub, weapon.HandAxe, weapon.Javelin,
                    weapon.LightHammer, weapon.Mace, weapon.Quarterstaff,
                    weapon.Sickle, weapon.Spear]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [pack.DungeoneersPack, pack.ExplorersPack]
            }),
            ('choose_skills', {
                'num': 3,
                'options': skills
            }),
        ],
        [   #Level 1
            ('add_feats', {'feats': ['Favored Enemy', 'Natural Explorer']}),
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