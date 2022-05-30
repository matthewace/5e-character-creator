"""Module to manage various Sizes of Characters and Creatures

https://roll20.net/compendium/dnd5e/Monsters#content
    Size	    Space	        Examples
    ----------------------------------------------
    Tiny	    2.5 x 2.5 ft.   Imp, Sprite
    Small	    5 x 5 ft.	    Giant Rat, Goblin
    Medium	    5 x 5 ft.	    Orc, Werewolf
    Large	    10 x 10 ft.	    Hippogriff, Ogre
    Huge	    15 x 15 ft.	    Fire Giant, Treant
    Gargantuan	20 x 20 ft.     Kraken, Purple Worm
"""


class Size:
    """Generic Size class to be sub-classed"""
    name = str
    size = float


class Tiny(Size):
    name = "Tiny"
    size = 2.5


class Small(Size):
    name = "Small"
    size = 5.0


class Medium(Size):
    name = "Medium"
    size = 5.0


class Large(Size):
    name = "Large"
    size = 10.0


class Huge(Size):
    name = "Huge"
    size = 15.0


class Gargantuan(Size):
    name = "Gargantuan"
    size = 20.0