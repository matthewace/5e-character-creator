"""Module for all types of Adventuring Gear.

    Ammunition
    Arcane Focus
    Common Gear
    Container
    Druidic Focus
    Holy Symbol
"""

from .ammunition import (Arrow, BlowgunNeedle, CrossbowBolt, SlingBullet)
from .arcane_focus import (Crystal, Orb, Rod, Staff, Wand)
from .common_gear import (
    Abacus, AcidVial, AlchemistsFire, AlmsBox, Antitoxin, BallBearings,
    Bedroll, Bell, Blanket, BlockAndTackle, Book, Caltrops, Candle, Censer,
    CrossbowBoltCase, ScrollCase, Chain, Chalk, ClimbersKit, CommonClothes,
    CostumeClothes, FineClothes, TravelersClothes, ComponentPouch, Crowbar,
    FishingTackle, GrapplingHook, Hammer, SledgeHammer, HealersKit, HolyWater,
    Hourglass, HuntingTrap, InkBottle, InkPen, Incense, Ladder, Lamp,
    LittleSandbag, LoreBook, BullseyeLantern, HoodedLantern, Lock,
    MagnifyingGlass, Manacles, MessKit, SteelMirror, OilFlask, PaperSheet,
    Parchment, Perfume, MinersPick, Piton, BasicPoison, Pole, HealingPotion,
    Quiver, PortableRam, Rations, Robes, HempenRope, SilkRope, MerchantsScale,
    SealingWax, Shovel, SignalWhistle, SignetRing, SmallKnife, Soap, Spellbook,
    IronSpikes, Spyglass, String, Tent, Tinderbox, Torch, Vestments, Whetstone,
    PrayerBook
)
from .container import (
    Backpack, Barrel, Basket, Bucket, Chest, Flask, GlassBottle, IronPot, Jug,
    Pitcher, Pouch, Purse, Sack, Tankard, Vial, Waterskin
)
from .druidic_focus import (SprigOfMistletoe, Totem, WoodenStaff, YewWand)
from .holy_symbol import (Amulet, Emblem, Reliquary)


__all__ = [
    'Abacus', 'AcidVial', 'AlchemistsFire', 'AlmsBox', 'Amulet', 'Antitoxin',
    'Arrow', 'Backpack', 'BallBearings', 'Barrel', 'BasicPoison', 'Basket',
    'Bedroll', 'Bell', 'Blanket', 'BlockAndTackle', 'BlowgunNeedle', 'Book',
    'Bucket', 'BullseyeLantern', 'Caltrops', 'Candle', 'Censer', 'Chain',
    'Chalk', 'Chest', 'ClimbersKit', 'CommonClothes', 'ComponentPouch',
    'CostumeClothes', 'CrossbowBolt', 'CrossbowBoltCase', 'Crowbar', 'Crystal',
    'Emblem', 'FineClothes', 'FishingTackle', 'Flask', 'GlassBottle',
    'GrapplingHook', 'Hammer', 'HealersKit', 'HealingPotion', 'HempenRope',
    'HolyWater', 'HoodedLantern', 'Hourglass', 'HuntingTrap', 'InkBottle',
    'InkPen',  'Incense', 'IronPot', 'IronSpikes', 'Jug', 'Ladder', 'Lamp',
    'LittleSandbag', 'Lock', 'LoreBook', 'MagnifyingGlass', 'Manacles',
    'MerchantsScale', 'MessKit', 'MinersPick', 'OilFlask', 'Orb', 'PaperSheet',
    'Parchment', 'Perfume', 'Pitcher', 'Piton', 'Pole', 'PortableRam', 'Pouch',
    'Purse', 'PrayerBook', 'Quiver', 'Rations', 'Reliquary', 'Robes', 'Rod',
    'Sack', 'ScrollCase', 'SealingWax', 'Shovel', 'SignalWhistle',
    'SignetRing', 'SilkRope', 'SledgeHammer', 'SlingBullet', 'SmallKnife',
    'Soap', 'Spellbook', 'SprigOfMistletoe', 'Spyglass', 'Staff',
    'SteelMirror', 'String', 'Tankard', 'Tent', 'Tinderbox', 'Torch', 'Totem',
    'TravelersClothes', 'Vial', 'Vestments', 'Wand', 'Waterskin', 'Whetstone',
    'WoodenStaff', 'YewWand',
]


GEAR_MAP = {
    'abacus': Abacus,
    'acidvial': AcidVial,
    'alchemistsfire': AlchemistsFire,
    'almsbox': AlmsBox,
    'amulet': Amulet,
    'antitoxin': Antitoxin,
    'arrow': Arrow,
    'backpack': Backpack,
    'ballbearings': BallBearings,
    'barrel': Barrel,
    'basicpoison': BasicPoison,
    'basket': Basket,
    'bedroll': Bedroll,
    'bell': Bell,
    'blanket': Blanket,
    'blockandtackle': BlockAndTackle,
    'blowgunneedle': BlowgunNeedle,
    'book': Book,
    'bucket': Bucket,
    'bullseyelantern': BullseyeLantern,
    'caltrops': Caltrops,
    'candle': Candle,
    'censer': Censer,
    'chain': Chain,
    'chalk': Chalk,
    'chest': Chest,
    'climberskit': ClimbersKit,
    'commonclothes': CommonClothes,
    'componentpouch': ComponentPouch,
    'costumeclothes': CostumeClothes,
    'crossbowbolt': CrossbowBolt,
    'crossbowboltcase': CrossbowBoltCase,
    'crowbar': Crowbar,
    'crystal': Crystal,
    'emblem': Emblem,
    'fineclothes': FineClothes,
    'fishingtackle': FishingTackle,
    'flask': Flask,
    'glassbottle': GlassBottle,
    'grapplinghook': GrapplingHook,
    'hammer': Hammer,
    'healerskit': HealersKit,
    'healingpotion': HealingPotion,
    'hempenrope': HempenRope,
    'holywater': HolyWater,
    'hoodedlantern': HoodedLantern,
    'hourglass': Hourglass,
    'huntingtrap': HuntingTrap,
    'incense': Incense,
    'inkbottle': InkBottle,
    'inkpen': InkPen,
    'ironpot': IronPot,
    'ironspikes': IronSpikes,
    'jug': Jug,
    'ladder': Ladder,
    'lamp': Lamp,
    'littlesandbag': LittleSandbag,
    'lock': Lock,
    'lorebook': LoreBook,
    'magnifyingglass': MagnifyingGlass,
    'manacles': Manacles,
    'merchantsscale': MerchantsScale,
    'messkit': MessKit,
    'minerspick': MinersPick,
    'oilflask': OilFlask,
    'orb': Orb,
    'papersheet': PaperSheet,
    'parchment': Parchment,
    'perfume': Perfume,
    'pitcher': Pitcher,
    'piton': Piton,
    'pole': Pole,
    'portableram': PortableRam,
    'pouch': Pouch,
    'quiver': Quiver,
    'rations': Rations,
    'reliquary': Reliquary,
    'robes': Robes,
    'rod': Rod,
    'sack': Sack,
    'scrollcase': ScrollCase,
    'sealingwax': SealingWax,
    'shovel': Shovel,
    'signalwhistle': SignalWhistle,
    'signetring': SignetRing,
    'silkrope': SilkRope,
    'sledgehammer': SledgeHammer,
    'slingbullet': SlingBullet,
    'smallknife': SmallKnife,
    'soap': Soap,
    'spellbook': Spellbook,
    'sprigofmistletoe': SprigOfMistletoe,
    'spyglass': Spyglass,
    'staff': Staff,
    'steelmirror': SteelMirror,
    'string': String,
    'tankard': Tankard,
    'tent': Tent,
    'tinderbox': Tinderbox,
    'torch': Torch,
    'totem': Totem,
    'travelersclothes': TravelersClothes,
    'vestments': Vestments,
    'vial': Vial,
    'wand': Wand,
    'waterskin': Waterskin,
    'whetstone': Whetstone,
    'woodenstaff': WoodenStaff,
    'yewwand': YewWand,
}


class GearHandler:
    """Class to assist in managing Gear objects"""
    pass