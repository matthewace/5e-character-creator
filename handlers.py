"""Module for various module handlers

The idea here is to have a class for each major chracter attribute to make
choosing easier.
"""

import os
import random
from typing import Dict

from dnd.backgrounds import BACKGROUND_MAP
from dnd.classes import CLASS_MAP
from dnd.races import RACE_MAP
from dnd.races.alignments import ALIGNMENT_MAP


class DndHandler:
    class_map = Dict
    class_type = str

    def __init__(self):
        self.str_names = _str_names()
        self.cls_names = _cls_names()
        self.type = self.class_type

    @classmethod
    def get_by_name(cls, name: str):
        """Returns a class object based on name.  The name can be either the
        name of the class, or the string represented name.
        """
        str_names = [c.name for c in cls.class_map.values()]
        cls_names = [c.__name__ for c in cls.class_map.values()]
        if name in str_names:
            _i = str_names.index(name)
            name = cls_names[_i]
        return cls.class_map.get(name.lower())

    @classmethod
    def choose(cls, randomize: bool = False):
        """Returns a class object based on user input of a choice.  The options
        are provided and an integer is entered to make the choice.

        Parameters
        ----------
        randomize : bool
            (Optional) If True, then the choice is randomized
        """
        str_names = [c.name for c in cls.class_map.values()]
        cls_names = [c.__name__ for c in cls.class_map.values()]
        name = ''
        if randomize:
            name = random.choice(str_names)
        else:
            os.system('clear')
            print(f'=== Select {cls.class_type} ===')
            for i in range(len(str_names)):
                print(f'{i}: {str_names[i]}')
            _i = -1
            while _i not in range(len(str_names)):
                try:
                    _i = int(input('Choose: '))
                except:
                    print('Integers Only!')
            name = str_names[_i]
        return cls.get_by_name(name)


class RaceHandler(DndHandler):
    class_map = RACE_MAP
    class_type = "Race"


class ClassHandler(DndHandler):
    class_map = CLASS_MAP
    class_type = "Class"


class BackgroundHandler(DndHandler):
    class_map = BACKGROUND_MAP
    class_type = "Background"


class AlignmentHandler(DndHandler):
    class_map = ALIGNMENT_MAP
    class_type = "Alignment"