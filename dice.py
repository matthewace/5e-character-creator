"""Module for managing various polyhedral dice

    D4, D6, D8, D10, D12, D20
"""

import random
import re
from functools import total_ordering
from typing import List, Tuple

from .troubleshoot import debug

@total_ordering
class PolyhedralDie:
    def __init__(self, sides: int):
        self.sides = sides
        self.name = f'd{self.sides}'
        self.face = 1

    def __str__(self):
        face = f'0{self.face}' if self.face < 10 else self.face            
        return f'{self.name} [{face}]'

    def __repr__(self):
        return f'{self.__class__}(sides={self.sides}, face={self.face})'

    def __eq__(self, other) -> bool:
        return (type(self) == type(other) 
                and self.sides == other.sides 
                and self.face == other.face)

    def __lt__(self, other) -> bool:
        return (type(self) == type(other)
                and self.face < other.face
                or (self.face == other.face and self.sides < other.sides))

    def roll(self, reroll_ones=False, cheat=False):
        """Roll the die

        Parameters
        ----------
        show : bool
            (Optional) If True, the die is printed after roll.
        reroll_ones : bool
            (Optional) If True, the die is re-rolled if a one is rolled.
        cheat : bool
            (Optional) If True, the maximum value is rolled.
        """
        if cheat:
            self.face = self.sides
        else:
            self.face = random.randint(1, self.sides)
            if reroll_ones and self.face == 1:
                self.roll(reroll_ones=True)


class DiceBag:
    """A manager of all the available Dice.  Useful functions for rolling 
    multiple Dice live here.
    """
    @classmethod
    def grab_dice(cls, dice_type) -> List[PolyhedralDie]:
        """Return multiple dice objects
        
        Parameters
        ----------
        dice_type : str or List[str]
            number and type of dice to grab
            ex: '2d8'; 'd20'; ['2d6', '1d4']
        """
        dice = []
        if type(dice_type) == list:
            for _dice in dice_type:
                dice += cls.grab_dice(_dice)
        elif type(dice_type) == str:
            result = re.search(r'(\d+)[Dd](\d+)', dice_type)
            if result:
                num, sides = result.groups()
                dice = [PolyhedralDie(int(sides)) for _ in range(int(num))]
        elif isinstance(dice_type, PolyhedralDie):
            dice = [dice_type]
        else:
            raise TypeError(f'unsupported type: grab_dice({type(dice_type)}')
        return dice

    @classmethod
    def roll_dice(cls, dice, show=False, drop_low=False, **kwargs) -> int:
        """Roll dice and get results

        Parameters
        ----------
        dice : str or List[str] or PolyhedralDie or List[PolyhedralDie]
            Dice to be rolled
        show : bool
            (Optional) If True, the results are printed
        drop_low : bool
            (Optional) If True, the lowest roll is dropped

        Returns
        -------
        roll_total : int
            The total value of all rolled dice
        """
        roll_total = 0
        
        dice = cls.grab_dice(dice)
        for die in dice:
            die.roll(**kwargs)
        dice.sort()
        dropped = dice.pop(0) if drop_low else None
        roll_total = sum([die.face for die in dice])
        if show:
            print(f'{cls._show(dice, dropped=dropped)} Total: {roll_total}')
        return roll_total

    @classmethod
    def roll_advantage(cls, show=False, **kwargs) -> int:
        """Roll 2d20 with advantage (Returns higher score)"""
        return cls.roll_dice('2d20', show=show, drop_low=True, **kwargs)

    @classmethod
    def roll_disadvantage(cls, show=False, **kwargs) -> int:
        """Roll 2d20 with disadvantage (Returns lower score)"""
        dice = cls.grab_dice('2d20')
        cls.roll_dice(dice, **kwargs)
        dice.sort(reverse=True)
        dropped = dice.pop(0)
        roll_total = dice[0].face
        if show:
            print(f'{cls._show(dice, dropped=dropped)} Total: {roll_total}')
        return roll_total

    def _show(dice, dropped=None) -> str:
        """Returns string representation of rolled dice

        Parameters
        ----------
        dice : List[PolyhedralDie]
            Dice to be shown in results
        dropped : PolyhedralDie
            (Optional) Dice dropped from roll
        """
        out = []
        results = {}
        for die in dice:
            if die.name not in results:
                results[die.name] = []
            results[die.name].append(die.face)
        for k, v in results.items():
            faces = ' '.join([f'[{i}]' for i in sorted(v)])
            if dropped and dropped.name == k:
                faces += f' ({dropped.face})'
            out.append(f'{k}: {faces}')
        return ' | '.join(out)