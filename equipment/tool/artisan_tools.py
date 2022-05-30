"""Artisan's Tools

    AlchemistsSupplies, BrewersSupplies, CalligraphersSupplies,
    CarpentersTools, CartographersTools, CobblersTools, CooksUtensils,
    GlassblowersTools, JewelersTools, LeatherworkersTools, MasonsTools,
    PaintersSupplies, PottersTools, SmithsTools, TinkersTools, WeaversTools,
    WoodcarversTools
"""

from dnd.equipment.base_equipment import Tool


class ArtisanTool(Tool):
    """Base class for Artisan Tools"""
    item_type = 'Artisan Tool'


class AlchemistsSupplies(ArtisanTool):
    name = 'Alchemist\'s Supplies'
    base_cost = '50 gp'
    base_weight = 8


class BrewersSupplies(ArtisanTool):
    name = 'Brewer\'s Supplies'
    base_cost = '20 gp'
    base_weight = 5


class CalligraphersSupplies(ArtisanTool):
    name = 'Caligrapher\'s Supplies'
    base_cost = '10 gp'
    base_weight = 5


class CarpentersTools(ArtisanTool):
    name = 'Carpenter\'s Tools'
    base_cost = '8 gp'
    base_weight = 6


class CartographersTools(ArtisanTool):
    name = 'Cartographer\'s Tools'
    base_cost = '15 gp'
    base_weight = 6


class CobblersTools(ArtisanTool):
    name = 'Cobbler\'s Tools'
    base_cost = '5 gp'
    base_weight = 5


class CooksUtensils(ArtisanTool):
    name = 'Cook\'s Utensils'
    base_cost = '1 gp'
    base_weight = 8


class GlassblowersTools(ArtisanTool):
    name = 'Glassblower\'s Tools'
    base_cost = '30 gp'
    base_weight = 5


class JewelersTools(ArtisanTool):
    name = 'Jeweler\'s Tools'
    base_cost = '25 gp'
    base_weight = 2


class LeatherworkersTools(ArtisanTool):
    name = 'Leatherworker\'s Tools'
    base_cost = '5 gp'
    base_weight = 5


class MasonsTools(ArtisanTool):
    name = 'Mason\'s Tools'
    base_cost = '10 gp'
    base_weight = 8


class PaintersSupplies(ArtisanTool):
    name = 'Painter\'s Supplies'
    base_cost = '10 gp'
    base_weight = 5


class PottersTools(ArtisanTool):
    name = 'Potter\'s Tools'
    base_cost = '10 gp'
    base_weight = 3


class SmithsTools(ArtisanTool):
    name = 'Smith\'s Tools'
    base_cost = '20 gp'
    base_weight = 8


class TinkersTools(ArtisanTool):
    name = 'Tinker\'s Tools'
    base_cost = '50 gp'
    base_weight = 10


class WeaversTools(ArtisanTool):
    name = 'Weaver\'s Tools'
    base_cost = '1 gp'
    base_weight = 5


class WoodcarversTools(ArtisanTool):
    name = 'Woodcarver\'s Tools'
    base_cost = '1 gp'
    base_weight = 5
