"""Module for various Ammunition types.  Ammunition will be represented as a
bundle such as 20 Arrows or 50 blow-gun needles.

    Arrow, BlowgunNeedle, CrossbowBolt, SlingBullet

Unique Class Parameters
-----------------------
base_bundle_size : int
    How many round of ammunition are included in the bundle
"""

from dnd.equipment.base_equipment import AdventuringGear


class Ammunition(AdventuringGear):
    """Base Ammunition Class"""
    item_type = 'Ammunition'
    base_bundle_size = int

    def __init__(self):
        super().__init__()
        self.bundle_size = self.base_bundle_size

    def __str__(self):
        return f'{super().__str__()}' +\
               f'Size: {self.bundle_size}'


class Arrow(Ammunition):
    name = 'Arrows'
    base_cost = '1 gp'
    base_weight = 1
    base_bundle_size = 20

    
class BlowgunNeedle(Ammunition):
    name = 'Blowgun Needles'
    base_cost = '1 gp'
    base_weight = 1
    base_bundle_size = 50


class CrossbowBolt(Ammunition):
    name = 'Crossbow Bolts'
    base_cost = '1 gp'
    base_weight = 1.5
    base_bundle_size = 20


class SlingBullet(Ammunition):
    name = 'Sling Bullets'
    base_cost = '4 cp'
    base_weight = 1.5
    base_bundle_size = 20