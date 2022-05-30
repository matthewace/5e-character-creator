"""Gaming sets

    Dice, Dragonchess, PlayingCards, ThreeDragonAnte
"""

from dnd.equipment.base_equipment import Tool


class GamingSet(Tool):
    """Base class for Gaming Sets"""
    item_type = 'Gaming Set'


class Dice(GamingSet):
    name = 'Dice Set'
    base_cost = '1 sp'
    base_weight = 0


class Dragonchess(GamingSet):
    name = 'Dragonchess Set'
    base_cost = '1 gp'
    base_weight = 0.5


class PlayingCards(GamingSet):
    name = 'Playing Cards'
    base_cost = '5 sp'
    base_weight = 0


class ThreeDragonAnte(GamingSet):
    name = 'Three-Dragon Ante Set'
    base_cost = '1 gp'
    base_weight = 0