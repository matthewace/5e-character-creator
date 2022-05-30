from .characterclass import CharacterClass
from dnd.equipment import *
from dnd.skills import *


class Warlock(CharacterClass):
    name = "Warlock"
    hit_die = '1d8'
    armor_proficiencies = [armor.LightArmor]
    weapon_proficiencies = [weapon.SimpleWeapon]
    tool_proficiencies = []
    saving_throws = ['WIS', 'CHA']
    skills = [
        Arcana, Deception, History, Intimidation, Investigation, Nature,
        Religion
    ]
    level = [
        [   #Level 0
            ('add_proficiencies', {
                'items': [
                armor_proficiencies, tool_proficiencies, weapon_proficiencies]
            }),
            ('add_equipment', {
                'items': [armor.Leather, [weapon.Dagger] * 2]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    [weapon.LightCrossbow, gear.CrossbowBolt], weapon.Club,
                    weapon.Dagger, weapon.GreatClub, weapon.HandAxe,
                    weapon.Javelin, weapon.LightHammer, weapon.Mace,
                    weapon.Quarterstaff, weapon.Sickle, weapon.Spear,
                    weapon.LightCrossbow, weapon.Dart, weapon.Shortbow,
                    weapon.Sling]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    weapon.Club, weapon.Dagger, weapon.GreatClub,
                    weapon.HandAxe, weapon.Javelin, weapon.LightHammer,
                    weapon.Mace, weapon.Quarterstaff, weapon.Sickle,
                    weapon.Spear, weapon.LightCrossbow, weapon.Dart,
                    weapon.Shortbow, weapon.Sling]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    gear.ComponentPouch, gear.Crystal, gear.Orb, gear.Rod,
                    gear.Staff, gear.Wand]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [pack.ScholarsPack, pack.DungeoneersPack]
            }),
            ('choose_skills', {
                'num': 2,
                'options': skills
            }),
        ],
        [   #Level 1
            ('add_feats', {'feats': ['Otherworldly Patron', 'Pact Magic']}),
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