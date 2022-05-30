import os
import random

from .sizes import Size, Tiny, Small, Medium, Large, Huge, Gargantuan

__all__ = [
    'Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan'
]

CLASS_MAP = {
    'tiny': Tiny,
    'Small': Small,
    'Medium': Medium,
    'Large': Large,
    'Huge': Huge,
    'Gargantuan': Gargantuan,
}

def ClassHandler(name: str = None, roll_random: bool = False) -> Size:
    """Function returns the proper CharacterRace by name"""
    if name and name.lower() in CLASS_MAP:
        return CLASS_MAP[name.lower()]
    if roll_random:
        return random.choice(list(CLASS_MAP.values()))
    choices = '\n'.join([f'{i}: {__all__[i]}' for i in range(len(__all__))])
    choice = -1
    while choice not in range(len(__all__)):
        try:
            os.system('clear')
            print(choices)
            choice = int(input("Choose: "))
        except:
            continue
    return CLASS_MAP[__all__[choice].lower()]