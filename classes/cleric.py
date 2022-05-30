from .characterclass import CharacterClass
from dnd.equipment import *
from dnd.skills import *


class Cleric(CharacterClass):
    name = "Cleric"
    hit_die = '1d8'
    armor_proficiencies = [armor.LightArmor, armor.MediumArmor, armor.Shield]
    tool_proficiencies = []
    weapon_proficiencies = [weapon.SimpleWeapon]
    saving_throws = ['WIS', 'CHA']
    skills = [History, Insight, Medicine, Persuasion, Religion]
    level = [
        [   #Level 0
            ('add_proficiencies', {
                'items': [
                armor_proficiencies, tool_proficiencies, weapon_proficiencies]
            }),
            ('add_equipment', {
                'items': armor.Shield
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [gear.Amulet, gear.Emblem, gear.Reliquary]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [pack.ExplorersPack, pack.PriestsPack]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [weapon.Mace, weapon.Warhammer]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    [weapon.LightCrossbow, gear.CrossbowBolt],
                    weapon.Club, weapon.Dagger, weapon.GreatClub,
                    weapon.HandAxe, weapon.Javelin, weapon.LightHammer,
                    weapon.Mace, weapon.Quarterstaff, weapon.Sickle,
                    weapon.Spear, weapon.Dart, weapon.Shortbow, weapon.Sling
                ]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [armor.ScaleMail, armor.Leather, armor.ChainMail]
            }),
            ('choose_skills', {
                'num': 2,
                'options': skills
            }),
        ],
        [   #Level 1
            ('add_feats', {'feats': ['Spellcasting', 'Divine Domain']}),
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