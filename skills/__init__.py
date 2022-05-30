import os
import random

from .skills import (Acrobatics, AnimalHandling, Arcana, Athletics,
                     Deception, History, Insight, Intimidation, Investigation,
                     Medicine, Nature, Perception, Performance, Persuasion,
                     Religion, SleightOfHand, Stealth, Survival, Skill)

__all__ = [
    'Acrobatics', 'AnimalHandling', 'Arcana', 'Athletics', 'Deception',
    'History', 'Insight', 'Intimidation', 'Investigation', 'Medicine', 'Nature',
    'Perception', 'Performance', 'Persuasion', 'Religion', 'SleightOfHand',
    'Stealth', 'Survival', 'Skill'
]

CLASS_MAP = {
    'acrobatics': Acrobatics,
    'animalhandling': AnimalHandling,
    'arcana': Arcana,
    'athletics': Athletics,
    'deception': Deception,
    'history': History,
    'insight': Insight,
    'intimidation': Intimidation,
    'investigation': Investigation,
    'medicine': Medicine,
    'nature': Nature,
    'perception': Perception,
    'performance': Performance,
    'persuasion': Persuasion,
    'religion': Religion,
    'sleightofhand': SleightOfHand,
    'stealth': Stealth,
    'survival': Survival
}

def ClassHandler(name: str = None, roll_random: bool = False):
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