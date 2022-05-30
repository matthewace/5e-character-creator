from .mounts import (Camel, Donkey, Elephant, DraftHorse, RidingHorse, Mastiff,
                     Pony, WarHorse, Mount)
from .vehicles import (Keelboat, Longship, Rowboat, Sailingship, Warship,
                       Carriage, Cart, Chariot, Sled, Wagon, WaterborneVehicle,
                       LandVehicle)

__all__ = [
    'Camel', 'Carriage', 'Cart', 'Chariot', 'Donkey', 'Elephant', 'DraftHorse',
    'Keelboat', 'LandVehicle', 'Longship', 'Mastiff', 'Mount', 'Pony',
    'RidingHorse', 'Rowboat', 'Sailingship', 'Sled', 'Wagon',
    'WaterborneVehicle', 'WarHorse', 'Warship'
]

MOUNT_MAP = {
    'camel': Camel,
    'donkey': Donkey,
    'drafthorse': DraftHorse,
    'elephant': Elephant,
    'mastiff': Mastiff,
    'pony': Pony,
    'ridinghorse': RidingHorse,
    'warhorse': WarHorse,
}

VEHICLE_MAP = {
    'carriage': Carriage,
    'cart': Cart,
    'chartiot': Chariot,
    'keelboat': Keelboat,
    'longship': Longship,
    'rowboat': Rowboat,
    'sailingship': Sailingship,
    'sled': Sled,
    'wagon': Wagon,
    'warship': Warship,
}


class MountHandler:
    """Assisting class to manage Mount objects"""
    pass


class VehicleHandler:
    """Assisting class tomanage Vehicle objects"""
    pass