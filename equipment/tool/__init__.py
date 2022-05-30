from .artisan_tools import (
    AlchemistsSupplies, BrewersSupplies, CalligraphersSupplies,
    CarpentersTools, CartographersTools, CobblersTools, CooksUtensils,
    GlassblowersTools, JewelersTools, LeatherworkersTools, MasonsTools,
    PaintersSupplies, PottersTools, SmithsTools, TinkersTools, WeaversTools,
    WoodcarversTools
)
from .gaming_sets import (
    Dice, Dragonchess, PlayingCards, ThreeDragonAnte
)
from .kits import (
    DisguiseKit, ForgeryKit, HerbalismKit, NavigatorsTools, PoisonersKit,
    ThievesTools
)
from .musical_instruments import (
    Bagpipes, Drum, Dulcimer, Flute, Lute, Lyre, Horn, PanFlute, Shawm, Viol
)

__all__ = [
    'AlchemistsSupplies', 'BrewersSupplies', 'CalligraphersSupplies',
    'CarpentersTools', 'CartographersTools', 'CobblersTools', 'CooksUtensils',
    'GlassblowersTools', 'JewelersTools', 'LeatherworkersTools', 'MasonsTools',
    'PaintersSupplies', 'PottersTools', 'SmithsTools', 'TinkersTools',
    'WeaversTools', 'WoodcarversTools', 'Dice', 'Dragonchess', 'PlayingCards',
    'ThreeDragonAnte', 'DisguiseKit', 'ForgeryKit', 'HerbalismKit',
    'NavigatorsTools', 'PoisonersKit', 'ThievesTools', 'Bagpipes', 'Drum',
    'Dulcimer', 'Flute', 'Lute', 'Lyre', 'Horn', 'PanFlute', 'Shawm', 'Viol',
]

ARTISAN_TOOL_MAP = {
    'alchemistssupplies': AlchemistsSupplies,
    'brewerssupplies': BrewersSupplies,
    'calligrapherssupplies': CalligraphersSupplies,
    'carpenterstools': CarpentersTools,
    'cartographerstools': CartographersTools,
    'cobblerstools': CobblersTools,
    'cooksutensils': CooksUtensils,
    'glassblowerstools': GlassblowersTools,
    'jewelerstools': JewelersTools,
    'leatherworkerstools': LeatherworkersTools,
    'masonstools': MasonsTools,
    'painterssupplies': PaintersSupplies,
    'potterstools': PottersTools,
    'smithstools': SmithsTools,
    'tinkerstools': TinkersTools,
    'weaverstools': WeaversTools,
    'woodcarverstools': WoodcarversTools,
}

GAMING_SET_MAP = {
    'dice': Dice,
    'dragonchess': Dragonchess,
    'playingcards': PlayingCards,
    'threedragonante': ThreeDragonAnte,
}

KIT_MAP = {
    'disguisekit': DisguiseKit,
    'forgerykit': ForgeryKit,
    'herbalismkit': HerbalismKit,
    'navigatorstools': NavigatorsTools,
    'poisonerskit': PoisonersKit,
    'thievestools': ThievesTools,
}

MUSICAL_INSTRUMENT_MAP = {
    'bagpipes': Bagpipes,
    'drum': Drum,
    'dulcimer': Dulcimer,
    'flute': Flute,
    'lute': Lute,
    'lyre': Lyre,
    'horn': Horn,
    'panflute': PanFlute,
    'shawm': Shawm,
    'viol': Viol,
}


class ToolHandler:
    """Class to assist in Tool management"""
    pass