from .characterclass import CharacterClass
from dnd.equipment import *
from dnd.skills import *


class Monk(CharacterClass):
    name = "Monk"
    hit_die = '1d8'
    armor_proficiencies = []
    tool_proficiencies = []
    weapon_proficiencies = [weapon.SimpleWeapon, weapon.Shortsword]
    saving_throws = ['STR', 'DEX']
    skills = [Acrobatics, Athletics, History, Insight, Religion, Stealth]
    level = [
        [   #Level 0
            ('add_proficiencies', {
                'items': [
                armor_proficiencies, tool_proficiencies, weapon_proficiencies]
            }),
            ('add_equipment', {
                'items': weapon.Dart
            }),
            ('choose_proficiencies', {
                'num': 1,
                'options': [
                    tool.AlchemistsSupplies, tool.BrewersSupplies,
                    tool.CalligraphersSupplies, tool.CarpentersTools,
                    tool.CartographersTools, tool.CobblersTools,
                    tool.CooksUtensils, tool.GlassblowersTools,
                    tool.JewelersTools, tool.LeatherworkersTools,
                    tool.MasonsTools, tool.PaintersSupplies, tool.PottersTools,
                    tool.SmithsTools, tool.TinkersTools, tool.WeaversTools,
                    tool.WoodcarversTools, tool.Bagpipes, tool.Drum,
                    tool.Dulcimer, tool.Flute, tool.Lute, tool.Lyre, tool.Horn,
                    tool.PanFlute, tool.Shawm, tool.Viol]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [
                    weapon.Shortsword, weapon.Club, weapon.Dagger,
                    weapon.GreatClub, weapon.HandAxe, weapon.Javelin,
                    weapon.LightHammer, weapon.Mace, weapon.Quarterstaff,
                    weapon.Sickle, weapon.Spear, weapon.LightCrossbow,
                    weapon.Dart, weapon.Shortbow, weapon.Sling]
            }),
            ('choose_equipment', {
                'num': 1,
                'options': [pack.DungeoneersPack, pack.ExplorersPack]
            }),
            ('choose_skills', {
                'num': 2,
                'options': skills
            }),
        ],
        [   #Level 1
            ('add_feats', {'feats': ['Unarmored Defense', 'Martial Arts']}),
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