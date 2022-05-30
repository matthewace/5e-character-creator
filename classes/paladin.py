from .characterclass import CharacterClass
from dnd.equipment import *
from dnd.skills import *


class Paladin(CharacterClass):
    name = "Paladin"
    hit_die = '1d10'
    armor_proficiencies = [
        armor.LightArmor, armor.MediumArmor, armor.HeavyArmor, armor.Shield
    ]
    tool_proficiencies = []
    weapon_proficiencies = [weapon.SimpleWeapon, weapon.MartialWeapon]
    saving_throws = ['WIS', 'CHA']
    skills = [Athletics, Insight, Intimidation, Medicine, Persuasion, Religion]
    level = [
        [   #Level 0
            ('add_proficiencies', {
                'items': [
                armor_proficiencies, tool_proficiencies, weapon_proficiencies]
            }),
            ('add_equipment', {
                'items': armor.ChainMail
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [gear.Amulet, gear.Emblem, gear.Reliquary]
            }),
            ('choose_equipment', {
                'num': 2,
                'options': [
                    armor.Shield, weapon.Battleaxe, weapon.Flail,
                    weapon.Glaive, weapon.Greataxe, weapon.Greatsword,
                    weapon.Halberd, weapon.Lance, weapon.Longsword,
                    weapon.Maul, weapon.Morningstar, weapon.Pike,
                    weapon.Rapier, weapon.Scimitar, weapon.Shortsword,
                    weapon.Trident, weapon.Warpick, weapon.Warhammer,
                    weapon.Whip, weapon.Blowgun, weapon.HandCrossbow,
                    weapon.HeavyCrossbow, weapon.Longbow, weapon.Net
                ]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    [weapon.Javelin] * 5, weapon.Club, weapon.Dagger,
                    weapon.GreatClub, weapon.HandAxe, weapon.LightHammer,
                    weapon.Mace, weapon.Quarterstaff, weapon.Sickle,
                    weapon.Spear
                ]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [pack.PriestsPack, pack.ExplorersPack]
            }),
            ('choose_skills', {
                'num': 2,
                'options': skills
            }),
        ],
        [   #Level 1
            ('add_feats', {'feats': ['Divine Sense', 'Lay on Hands']}),
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