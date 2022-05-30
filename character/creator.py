"""Character Creator"""

import os
import random

from .character import Character
from dnd.dice import DiceBag
from dnd.handlers import AlignmentHandler
from dnd.handlers import BackgroundHandler
from dnd.handlers import ClassHandler
from dnd.handlers import RaceHandler


class Creator:
    """Character creator for basic vitals.  Can randomize choices or walk a
    user through picking each option.
    """
    def __init__(self) -> None:
        pass

    @classmethod
    def create_character(cls, randomize: bool = False):
        """Primary function of Creator class.  This function manages the
        process of creating a new character.

        Parameters
        ----------
        randomize : bool
            (optional) If set to True, then all options are random.
        """
        vitals = {}
        race = RaceHandler.choose(randomize=randomize)
        starting_class = ClassHandler.choose(randomize=randomize)
        background = BackgroundHandler.choose(randomize=randomize)
        sex = choose(['Male', 'Female'], c_type='Sex', randomize=randomize)[0]
        if not randomize:
            alignment = AlignmentHandler.choose()
            os.system('clear')
            name = input('Character Name: ')
        else:
            alignment = choose(race.alignments, randomize=True)
            fnames = race.male_names if sex == 'Male' else race.female_names
            fname = choose(fnames, randomize=True)[0]
            cname = choose(race.clan_names, randomize=True)[0]
            name = f'{fname} {cname}' if cname else fname

        height, weight = cls._roll_height_weight(race, randomize=randomize)
        
        vitals = {
            'name': name, 'race': race, 'starting_class': starting_class,
            'background': background, 'alignment': alignment, 'sex': sex,
            'height': height, 'weight': weight, 'randomize': randomize,
        }
        return Character(**vitals)

    def _roll_height_weight(race, randomize: bool = False):
        """Rolls for height and weight based on character Race"""
        h_die = race.height_mod
        w_die = race.weight_mod
        base_height = race.base_height
        base_weight = race.base_weight
        if randomize:
            height_roll = DiceBag.roll_dice(h_die)
            weight_roll = DiceBag.roll_dice(w_die)
            height = base_height + height_roll
            weight = base_weight + (height_roll * weight_roll)
        else:
            h_roll_max = DiceBag.roll_dice(h_die, cheat=True)
            w_roll_max = DiceBag.roll_dice(w_die, cheat=True)
            h_max = base_height + h_roll_max
            w_max = base_weight + (h_roll_max * w_roll_max)
            height = 0
            weight = 0
            details = [
                f'Height and Weight Entry: {race.name}',
                f'Height Range: {base_height} - {h_max}',
                f'Weight Range: {base_weight} - {w_max}',
            ]
            while True:
                os.system('clear')
                print('\n'.join(details))
                print(f'`r` to roll for stat...')
                entry = input('Enter Height (inches): ')
                if entry == 'r':
                    h_roll = DiceBag.roll_dice(h_die, show=True)
                    height = base_height + h_roll
                    details.append(f'Height Roll: {h_die}: {h_roll}')
                    break
                else:
                    try:
                        if int(entry) in range(base_height, h_max + 1):
                            height = entry
                            break
                    except:
                        continue
            details.append(f'Height: {height}')
            print(f'Height: {height}')
            input('Press Enter to continue...')
            while True:
                os.system('clear')
                print('\n'.join(details))
                print(f'`r` to roll for stat...')
                entry = input('Enter Weight (pounds): ')
                if entry == 'r':
                    w_roll = DiceBag.roll_dice(w_die, show=True)
                    if not h_roll:
                        h_roll = height - base_height
                    weight = base_weight + (h_roll * w_roll)
                    details.append(f'Weight Roll: {w_die}: {w_roll}')
                    break
                else:
                    try:
                        if int(entry) in range(base_weight, w_max + 1):
                            weight = entry
                            break
                    except:
                        continue
            details.append(f'Weight: {weight}')
            print(f'Weight: {weight}')
            input('Press Enter to continue...')

        return height, weight

    def _str_vitals(vitals: dict):
        out = []
        for k, v in vitals.items():
            k = 'Class' if k == 'starting_class' else k.capitalize()
            v = v if type(v) != type else v.name
            s = ' ' * (11 - len(k))
            out.append(f'{k}:{s}{v}')
        return '\n'.join(out)

def choose(options: list, 
           num: int = 1, 
           c_type: str = '', 
           randomize: bool = False):
    """Choose from a provided list of options

    Parameters
    ----------
    options : list
        List of objects to choose from
    num : int
        Number of choices to make
    c_type : str
        Type of objects to choose from.  Will be put in banner:
            `=== Choose {c_type} ===`
    """
    choices = []
    if num >= len(options):
        choices += options
    else:
        c_type = c_type if c_type else 'Option'
        while num > 0:
            choice = None
            if randomize:
                choice = random.choice(options)
            else:
                os.system('clear')
                print(f'=== Select {c_type} ===')
                for i in range(len(options)):
                    if type(options[i]) == str:
                        _opt = options[i]
                    else:
                        _opt = options[i].name
                    print(f'{i}: {_opt}')
                _i = -1
                while _i not in range(len(options)):
                    try:
                        _i = int(input('Choose: '))
                    except:
                        print('Integers Only!')
                choice = options[_i]
            choices.append(choice)
            num -= 1
    return choices