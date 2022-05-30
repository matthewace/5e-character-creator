"""Tool Kits

    DisguiseKit, ForgeryKit, HerbalismKit, NavigatorsTools, PoisonersKit,
    ThievesTools
"""

from dnd.equipment.base_equipment import Tool


class Kit(Tool):
    """Base class for Kit"""
    item_type = 'Kit'


class DisguiseKit(Kit):
    name = 'Disguise Kit'
    base_cost = '25 gp'
    base_weight = 3


class ForgeryKit(Kit):
    name = 'Forgery Kit'
    base_cost = '15 gp'
    base_weight = 5


class HerbalismKit(Kit):
    name = 'Herbalism Kit'
    base_cost = '5 gp'
    base_weight = 3


class NavigatorsTools(Kit):
    name = 'Navigator\'s Tools'
    base_cost = '25 gp'
    base_weight = 2


class PoisonersKit(Kit):
    name = 'Poisoner\'s Kit'
    base_cost = '50 gp'
    base_weight = 2


class ThievesTools(Kit):
    name = 'Thieve\'s Kit'
    base_cost = '25 gp'
    base_weight = 1