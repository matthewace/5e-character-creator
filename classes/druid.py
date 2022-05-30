from .characterclass import CharacterClass
from dnd.equipment import *
from dnd.skills import *


class Druid(CharacterClass):
    name = "Druid"
    hit_die = '1d8'
    armor_proficiencies = [armor.LightArmor, armor.MediumArmor, armor.Shield]
    tool_proficiencies = [tool.HerbalismKit]
    weapon_proficiencies = [
        weapon.Club, weapon.Dagger, weapon.Dart, weapon.Javelin, weapon.Mace,
        weapon.Quarterstaff, weapon.Scimitar, weapon.Sickle, weapon.Sling,
        weapon.Spear
    ]
    saving_throws = ['INT', 'WIS']
    skills = [
        AnimalHandling, Arcana,Insight, Medicine, Nature, Perception ,Religion,
        Survival
    ]
    level = [
        [   #Level 0
            ('add_proficiencies', {
                'items': [
                armor_proficiencies, tool_proficiencies, weapon_proficiencies]
            }),
            ('add_equipment', {
                'items': [armor.Leather, pack.ExplorersPack]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    gear.SprigOfMistletoe, gear.Totem, gear.WoodenStaff,
                    gear.YewWand]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    armor.Shield, weapon.Club, weapon.Dagger, weapon.GreatClub,
                    weapon.HandAxe, weapon.Javelin, weapon.LightHammer,
                    weapon.Mace, weapon.Quarterstaff, weapon.Sickle,
                    weapon.Spear, weapon.LightCrossbow, weapon.Dart,
                    weapon.Shortbow, weapon.Sling]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    weapon.Scimitar, weapon.Club, weapon.Dagger,
                    weapon.GreatClub, weapon.HandAxe, weapon.Javelin,
                    weapon.LightHammer, weapon.Mace, weapon.Quarterstaff,
                    weapon.Sickle, weapon.Spear]
            }),
            ('choose_skills', {
                'num': 2,
                'options': skills
            }),
        ],
        [   #Level 1
            ('add_feats', {'feats': ['Druidic', 'Spellcasting']}),
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