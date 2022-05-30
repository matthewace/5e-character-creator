from .armor import (
    BreastPlate, ChainMail, ChainShirt, HalfPlate, HeavyArmor, Hide, Leather,
    LightArmor, MediumArmor, Padded, Plate, RingMail, ScaleMail, Shield,
    Splint, StuddedLeather
)


__all__ = [
    'BreastPlate', 'ChainMail', 'ChainShirt', 'HalfPlate', 'HeavyArmor',
    'Hide', 'Leather', 'LightArmor', 'MediumArmor', 'Padded', 'Plate',
    'RingMail', 'ScaleMail', 'Shield', 'Splint', 'StuddedLeather'
]

ARMOR_MAP = {
    'breastplate': BreastPlate,
    'chainmail': ChainMail,
    'chainshirt': ChainShirt,
    'halfplate': HalfPlate,
    'hide': Hide,
    'leather': Leather,
    'padded': Padded,
    'plate': Plate,
    'ringmail': RingMail,
    'scalemail': ScaleMail,
    'shield': Shield,
    'splint': Splint,
    'studdedleather': StuddedLeather,
}


class ArmorHandler:
    pass