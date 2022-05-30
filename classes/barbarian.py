from .characterclass import CharacterClass
from dnd.equipment import *
from dnd.skills import *


class Barbarian(CharacterClass):
    name = "Barbarian"
    hit_die = '1d12'
    armor_proficiencies = [armor.LightArmor, armor.MediumArmor, armor.Shield]
    tool_proficiencies = []
    weapon_proficiencies = [weapon.SimpleWeapon, weapon.MartialWeapon]
    saving_throws = ['STR', 'CON']
    skills = [
        AnimalHandling, Athletics, Intimidation, Nature, Perception, Survival
    ]
    level = [
        [   #Level 0
            ('add_proficiencies', {
                'items': [
                armor_proficiencies, tool_proficiencies, weapon_proficiencies]
            }),
            ('add_equipment', {
                'items': [pack.ExplorersPack, [weapon.Javelin] * 4]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    weapon.Battleaxe, weapon.Flail, weapon.Glaive,
                    weapon.Greataxe, weapon.Greatsword, weapon.Halberd,
                    weapon.Lance, weapon.Longsword, weapon.Maul,
                    weapon.Morningstar, weapon.Pike, weapon.Rapier,
                    weapon.Scimitar, weapon.Shortsword, weapon.Trident,
                    weapon.Warpick, weapon.Warhammer, weapon.Whip]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    2 * [weapon.HandAxe], weapon.Club, weapon.Dagger,
                    weapon.GreatClub, weapon.Javelin, weapon.LightHammer,
                    weapon.Mace, weapon.Quarterstaff, weapon.Sickle,
                    weapon.Spear, weapon.LightCrossbow, weapon.Dart,
                    weapon.Shortbow, weapon.Sling]
            }),
            ('choose_skills', {
                'num': 2,
                'options': skills
            }),
        ],
        [   #Level 1
            ('add_feats', {'feats': ['Rage', 'Unarmored Defense']}),
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