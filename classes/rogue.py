from .characterclass import CharacterClass
from dnd.equipment import *
from dnd.skills import *


class Rogue(CharacterClass):
    name = "Rogue"
    hit_die = '1d8'
    armor_proficiencies = [armor.LightArmor]
    weapon_proficiencies = [
        weapon.SimpleWeapon, weapon.HandCrossbow, weapon.Longsword,
        weapon.Rapier, weapon.Shortsword
    ]
    tool_proficiencies = [tool.ThievesTools]
    saving_throws = ['DEX', 'INT']
    skills = [
        Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation,
        Perception, Performance, Persuasion, SleightOfHand, Stealth
    ]
    level = [
        [   #Level 0
            ('add_proficiencies', {
                'items': [
                armor_proficiencies, tool_proficiencies, weapon_proficiencies]
            }),
            ('add_equipment', {
                'items': [
                    armor.Leather, [weapon.Dagger] * 2, tool.ThievesTools]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [weapon.Rapier, weapon.Shortsword]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    [weapon.Shortbow, gear.Quiver, gear.Arrow],
                    weapon.Shortsword]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    pack.BurglarsPack, pack.DungeoneersPack,
                    pack.ExplorersPack]
            }),
            ('choose_skills', {
                'num': 4,
                'options': skills
            }),
        ],
        [   #Level 1
            ('add_feats', {
                'feats': ['Expertise', 'Sneak Attack', 'Thieves Cant']
            }),
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