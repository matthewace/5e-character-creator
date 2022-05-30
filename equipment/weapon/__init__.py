"""Package for managing Weapon objects."""

from .weapons import (
    Battleaxe, Blowgun, Club, Dagger, Dart, Flail, Glaive, Greataxe, GreatClub,
    Greatsword, Halberd, HandAxe, HandCrossbow, HeavyCrossbow, Javelin, Lance,
    LightCrossbow, LightHammer, Longbow, Longsword, Mace, MartialWeapon, Maul,
    Morningstar, Net, Pike, Quarterstaff, Rapier, Scimitar, Shortbow,
    Shortsword, Sickle, SimpleWeapon, Sling, Spear, Trident, Warhammer,
    Warpick, Whip,
)


__all__ = [
    'Battleaxe', 'Blowgun', 'Club', 'Dagger', 'Dart', 'Flail', 'Glaive',
    'Greataxe', 'GreatClub', 'Greatsword', 'Halberd', 'HandAxe',
    'HandCrossbow', 'HeavyCrossbow', 'Javelin', 'Lance', 'LightCrossbow',
    'LightHammer', 'Longbow', 'Longsword', 'Mace', 'MartialWeapon', 'Maul',
    'Morningstar', 'Net', 'Pike', 'Quarterstaff', 'Rapier', 'Scimitar',
    'Shortbow', 'Shortsword', 'Sickle', 'SimpleWeapon', 'Sling', 'Spear',
    'Trident', 'Warhammer', 'Warpick', 'Whip',
]

WEAPON_MAP = {
    'battleaxe': Battleaxe,
    'blowgun': Blowgun,
    'club': Club,
    'dagger': Dagger,
    'dart': Dart,
    'flail': Flail,
    'glaive': Glaive,
    'greatclub': GreatClub,
    'greatsword': Greatsword,
    'halberd': Halberd,
    'handaxe': HandAxe,
    'handcrossbow': HandCrossbow,
    'heavycrossbow': HeavyCrossbow,
    'javelin': Javelin,
    'lance': Lance,
    'lightcrossbow': LightCrossbow,
    'lighthammer': LightHammer,
    'longbow': Longbow,
    'longsword': Longsword,
    'mace': Mace,
    'maul': Maul,
    'morningstar': Morningstar,
    'net': Net,
    'pike': Pike,
    'quarterstaff': Quarterstaff,
    'rapier': Rapier,
    'scimitar': Scimitar,
    'shortbow': Shortbow,
    'shortsword': Shortsword,
    'sickle': Sickle,
    'sling': Sling,
    'spear': Spear,
    'trident': Trident,
    'warhammer': Warhammer,
    'warpick': Warpick,
    'whip': Whip,
}


class WeaponsHandler:
    """Class to assist in Weapon management"""
    pass