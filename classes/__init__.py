import os
import random

from .characterclass import CharacterClass
from .barbarian import Barbarian
from .bard import Bard
from .cleric import Cleric
from .druid import Druid
from .fighter import Fighter
from .monk import Monk
from .paladin import Paladin
from .ranger import Ranger
from .rogue import Rogue
from .sorcerer import Sorcerer
from .warlock import Warlock
from .wizard import Wizard

__all__ = [
    'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin',
    'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard',
]

CLASS_MAP = {
    'barbarian': Barbarian,
    'bard': Bard,
    'cleric': Cleric,
    'druid': Druid,
    'fighter': Fighter,
    'monk': Monk,
    'paladin': Paladin,
    'ranger': Ranger,
    'rogue': Rogue,
    'sorcerer': Sorcerer,
    'warlock': Warlock,
    'wizard': Wizard,
}