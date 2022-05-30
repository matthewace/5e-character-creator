import os
import random

from .baserace import CharacterRace
from .dragonborn import Dragonborn
from .dwarf import HillDwarf, MountainDwarf
from .elf import HighElf, WoodElf
from .gnome import ForestGnome, RockGnome
from .halfelf import HalfElf
from .halfling import Lightfoot, Stout
from .halforc import HalfOrc
from .human import Human
from .tiefling import Tiefling

__all__ = [
    'Dragonborn', 'ForestGnome', 'HalfElf', 'HalfOrc', 'HighElf', 'HillDwarf',
    'Human', 'Lightfoot', 'MountainDwarf', 'RockGnome', 'Stout', 'Tiefling',
    'WoodElf',
]

RACE_MAP = {
    'dragonborn': Dragonborn,
    'hilldwarf': HillDwarf,
    'mountaindwarf': MountainDwarf,
    'halfelf': HalfElf,
    'halforc': HalfOrc,
    'human': Human,
    'tiefling': Tiefling,
    'highelf': HighElf,
    'woodelf': WoodElf,
    'lightfoot': Lightfoot,
    'stout': Stout,
    'forestgnome': ForestGnome,
    'rockgnome': RockGnome,
}