import os
import random

from .language import Language
from .abyssal import Abyssal
from .celestial import Celestial
from .common import Common
from .deepspeech import DeepSpeech
from .draconic import Draconic
from .dwarvish import Dwarvish
from .elvish import Elvish
from .giant import Giant
from .gnomish import Gnomish
from .goblin import Goblin
from .halfling import Halfling
from .infernal import Infernal
from .orcish import Orcish
from .primordial import Primordial
from .sylvan import Sylvan
from .undercommon import Undercommon

__all__ = [
    'Abyssal', 'Celestial', 'Common', 'DeepSpeech', 'Draconic', 'Dwarvish',
    'Elvish', 'Giant', 'Gnomish', 'Goblin', 'Halfling', 'Infernal', 'Orcish',
    'Primordial', 'Sylvan', 'Undercommon'
]

CLASS_MAP = {
    'abyssal': Abyssal,
    'celestial': Celestial,
    'common': Common,
    'deepspeech': DeepSpeech,
    'draconic': Draconic,
    'dwarvish': Dwarvish,
    'elvish': Elvish,
    'giant': Giant,
    'gnomish': Gnomish,
    'goblin': Goblin,
    'halfling': Halfling,
    'infernal': Infernal,
    'orcish': Orcish,
    'primordial': Primordial,
    'sylvan': Sylvan,
    'undercommon': Undercommon,
}

CLASS_NAMES = [CLASS_MAP[r.lower()].name for r in __all__]

def ClassHandler(name: str = None, roll_random: bool = False) -> Language:
    """Function returns the proper CharacterRace by name"""
    if name and name.lower() in CLASS_MAP:
        return CLASS_MAP[name.lower()]
    if name and name in CLASS_NAMES:
        return CLASS_MAP[__all__[CLASS_NAMES.index(name)].lower()]
    if roll_random:
        return random.choice(list(CLASS_MAP.values()))

    choices = '\n'.join([f'{i}: {CLASS_NAMES[i]}' for i in range(len(__all__))])
    choice = -1
    while choice not in range(len(__all__)):
        try:
            os.system('clear')
            print(choices)
            choice = int(input("Choose Language: "))
        except:
            continue
    return CLASS_MAP[__all__[choice].lower()]