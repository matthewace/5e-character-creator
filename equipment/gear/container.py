"""Module for Container type items.  

    Backpack, Barrel, Basket, Bucket, Chest, Flask, GlassBottle, IronPot, Jug,
    Pitcher, Pouch, Sack, Tankard, Vial, Waterskin

Unique Class Parameters
-----------------
base_weight_capacity : int
    Maximum weight, in lbs, the container can hold
base_dry_volume : int
    Maximum volume, in cubic ft, of dry goods the container can hold
base_wet_volume : int
    Maximum volume, in pints, of liquid the container can hold
contents : List[AdventuringGear]
    Contents being carried in container
"""

from dnd.equipment.base_equipment import AdventuringGear


class Container(AdventuringGear):
    item_type = 'Container'
    base_weight_capacity = int
    base_dry_volume = float
    base_wet_volume = float

    def __init__(self, contents=[]):
        super().__init__()
        self.dry_volume = 0
        self.wet_volume = 0
        self.contents = contents
        self.contents_weight = self.get_weight()
    
    def __str__(self):
        return f'{super().__str__()}' +\
               f'{self.pretty_capacity()}\n' +\
               f'{self.pretty_contents()}\n'

    def get_weight(self) -> float:
        weight = 0
        for item in self.contents:
            try:
                weight += item.weight
            except:
                continue
        return weight

    def pretty_capacity(self) -> str:
        """Make a readable Capacity string"""
        out = []
        if self.base_dry_volume:
            out.append(f'{self.base_dry_volume} cubic feet')
        if self.base_weight_capacity:
            out.append(f'{self.base_weight_capacity} lbs')
        if self.base_wet_volume:
            out.append(f'{self.base_wet_volume} pints')
        return f'Capacity:  {", ".join(out)}'

    def pretty_contents(self) -> str:
        return f'Contents:  {", ".join([str(i) for i in self.contents])}'


class Backpack(Container):
    name = 'Backpack'
    base_cost = '2 gp'
    base_weight = 5
    base_weight_capacity = 30
    base_dry_volume = 1
    base_wet_volume = 0


class Barrel(Container):
    name = 'Barrel'
    base_cost = '2 gp'
    base_weight = 70
    base_weight_capacity = 0
    base_dry_volume = 4
    base_wet_volume = 40


class Basket(Container):
    name = 'Basket'
    base_cost = '4 sp'
    base_weight = 2
    base_weight_capacity = 40
    base_dry_volume = 2
    base_wet_volume = 0


class GlassBottle(Container):
    name = 'Glass Bottle'
    base_cost = '2 gp'
    base_weight = 2
    base_weight_capacity = 0
    base_dry_volume = 0
    base_wet_volume = 1.5


class Bucket(Container):
    name = 'Bucket'
    base_cost = '5 cp'
    base_weight = 2
    base_weight_capacity = 0
    base_dry_volume = 1.5
    base_wet_volume = 3


class Chest(Container):
    name = 'Chest'
    base_cost = '5 gp'
    base_weight = 25
    base_weight_capacity = 300
    base_dry_volume = 12
    base_wet_volume = 0


class Flask(Container):
    name = 'Flask'
    base_cost = '2 cp'
    base_weight = 1
    base_weight_capacity = 0
    base_dry_volume = 0
    base_wet_volume = 1


class Tankard(Container):
    name = 'Tankard'
    base_cost = '2 cp'
    base_weight = 1
    base_weight_capacity = 0
    base_dry_volume = 0
    base_wet_volume = 1


class Jug(Container):
    name = 'Jug'
    base_cost = '2 cp'
    base_weight = 4
    base_weight_capacity = 0
    base_dry_volume = 0
    base_wet_volume = 8


class Pitcher(Container):
    name = 'Pitcher'
    base_cost = '2 cp'
    base_weight = 4
    base_weight_capacity = 0
    base_dry_volume = 0
    base_wet_volume = 8


class IronPot(Container):
    name = 'Iron Pot'
    base_cost = '2 gp'
    base_weight = 10
    base_weight_capacity = 0
    base_dry_volume = 0
    base_wet_volume = 8


class Pouch(Container):
    name = 'Pouch'
    base_cost = '5 sp'
    base_weight = 1
    base_weight_capacity = 6
    base_dry_volume = 0.2
    base_wet_volume = 0


class Purse(Container):
    name = 'Purse'
    base_cost = '5 gp'
    base_weight = 2
    base_weight_capacity = 12
    base_dry_volume = 0.5
    base_wet_volume = 0


class Sack(Container):
    name = 'Sack'
    base_cost = '1 cp'
    base_weight = 0.5
    base_weight_capacity = 30
    base_dry_volume = 1
    base_wet_volume = 0


class Vial(Container):
    name = 'Vial'
    base_cost = '1 gp'
    base_weight = 0
    base_weight_capacity = 0
    base_dry_volume = 0
    base_wet_volume = 0.25


class Waterskin(Container):
    name = 'Waterskin'
    base_cost = '2 sp'
    base_weight = 1
    base_weight_capacity = 0
    base_dry_volume = 0
    base_wet_volume = 4