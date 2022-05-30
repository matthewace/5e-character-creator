"""Module for gear items that don't have a broader classification or may be
reclassified later.

    Abacus, AcidVial, AlchemistsFire, Antitoxin, BallBearings, Bedroll, Bell,
    Blanket, BlockAndTackle, Book, Caltrops, Candle, CrossbowBoltCase,
    ScrollCase, Chain, Chalk, ClimbersKit, CommonClothes, CostumeClothes,
    FineClothes, TravelersClothes, ComponentPouch, Crowbar, FishingTackle,
    GrapplingHook, Hammer, SledgeHammer, HealersKit, HolyWater, Hourglass,
    HuntingTrap, InkBottle, InkPen, Ladder, Lamp, BullseyeLantern,
    HoodedLantern, Lock, MagnifyingGlass, Manacles, MessKit, SteelMirror,
    OilFlask, PaperSheet, Parchment, Perfume, MinersPick, Piton, BasicPoison,
    Pole, HealingPotion, Quiver, PortableRam, Rations, Robes, HempenRope,
    SilkRope, MerchantsScale, SealingWax, Shovel, SignalWhistle, SignetRing,
    Soap, Spellbook, IronSpikes, Spyglass, String, Tent, Whetstone,
"""

from dnd.equipment.base_equipment import AdventuringGear


class CommonItem(AdventuringGear):
    item_type = 'Common Item'
    

class Abacus(CommonItem):
    name = 'Abacus'
    base_cost = '2 gp'
    base_weight = 2


class AcidVial(CommonItem):
    name = 'Acid (vial)'
    base_cost = '25 gp'
    base_weight = 1


class AlchemistsFire(CommonItem):
    name = 'Alchemist\'s Fire (Flask)'
    base_cost = '50 gp'
    base_weight = 1


class AlmsBox(CommonItem):
    name = 'Alms Box'
    base_cost = '0 cp'
    base_weight = 0


class Antitoxin(CommonItem):
    name = 'Antitoxin (vial)'
    base_cost = '50 gp'
    base_weight = 0


class BallBearings(CommonItem):
    name = 'Ball bearings (bag of 1,000)'
    base_cost = '1 gp'
    base_weight = 2


class Bedroll(CommonItem):
    name = 'Bedroll'
    base_cost = '1 gp'
    base_weight = 7


class Bell(CommonItem):
    name = 'Bell'
    base_cost = '1 gp'
    base_weight = 0


class Blanket(CommonItem):
    name = 'Blanket'
    base_cost = '5 sp'
    base_weight = 3


class BlockAndTackle(CommonItem):
    name = 'Block and Tackle'
    base_cost = '1 gp'
    base_weight = 5


class Book(CommonItem):
    name = 'Book'
    base_cost = '25 gp'
    base_weight = 5


class Caltrops(CommonItem):
    name = 'Caltrops (bag of 20)'
    base_cost = '1 gp'
    base_weight = 2


class Candle(CommonItem):
    name = 'Candle'
    base_cost = '1 cp'
    base_weight = 0


class Censer(CommonItem):
    name = 'Censer'
    base_cost = '0 cp'
    base_weight = 0


class CrossbowBoltCase(CommonItem):
    name = 'Case (Crossbow Bolt)'
    base_cost = '1 gp'
    base_weight = 1


class ScrollCase(CommonItem):
    name = 'Case (map or scroll)'
    base_cost = '1 gp'
    base_weight = 1


class Chain(CommonItem):
    name = 'Chain (10 feet)'
    base_cost = '5 gp'
    base_weight = 10


class Chalk(CommonItem):
    name = 'Chalk (1 piece)'
    base_cost = '1 cp'
    base_weight = 0


class ClimbersKit(CommonItem):
    name = 'Climber\'s Kit'
    base_cost = '25 gp'
    base_weight = 12


class CommonClothes(CommonItem):
    name = 'Clothes (common)'
    base_cost = '5 sp'
    base_weight = 3


class CostumeClothes(CommonItem):
    name = 'Clothes (costume)'
    base_cost = '5 gp'
    base_weight = 3


class FineClothes(CommonItem):
    name = 'Clothes (fine)'
    base_cost = '15 gp'
    base_weight = 6


class TravelersClothes(CommonItem):
    name = 'Clothes (traverler\'s)'
    base_cost = '2 gp'
    base_weight = 4


class ComponentPouch(CommonItem):
    name = 'Component Pouch'
    base_cost = '25 gp'
    base_weight = 2


class Crowbar(CommonItem):
    name = 'Crowbar'
    base_cost = '2 gp'
    base_weight = 5


class FishingTackle(CommonItem):
    name = 'Fishing Tackle'
    base_cost = '1 gp'
    base_weight = 4


class GrapplingHook(CommonItem):
    name = 'Grappling Hook'
    base_cost = '2 gp'
    base_weight = 4


class Hammer(CommonItem):
    name = 'Hammer'
    base_cost = '1 gp'
    base_weight = 3


class SledgeHammer(CommonItem):
    name = 'Hammer (sledge)'
    base_cost = '2 gp'
    base_weight = 10


class HealersKit(CommonItem):
    name = 'Healer\'s Kit'
    base_cost = '5 gp'
    base_weight = 3


class HolyWater(CommonItem):
    name = 'Holy Water (flask)'
    base_cost = '25 gp'
    base_weight = 1


class Hourglass(CommonItem):
    name = 'Hourglass'
    base_cost = '25 gp'
    base_weight = 1


class HuntingTrap(CommonItem):
    name = 'Hunting Trap'
    base_cost = '5 gp'
    base_weight = 25


class InkBottle(CommonItem):
    name = 'Ink (1 ounce bottle)'
    base_cost = '10 gp'
    base_weight = 0


class InkPen(CommonItem):
    name = 'Ink Pen'
    base_cost = '2 cp'
    base_weight = 4


class Incense(CommonItem):
    name = 'Block of Incense'
    base_cost = '0 cp'
    base_weight = 0


class Ladder(CommonItem):
    name = 'Ladder (10 foot)'
    base_cost = '1 sp'
    base_weight = 25


class Lamp(CommonItem):
    name = 'Lamp'
    base_cost = '5 sp'
    base_weight = 1


class BullseyeLantern(CommonItem):
    name = 'Lantern, bullseye'
    base_cost = '10 gp'
    base_weight = 2


class HoodedLantern(CommonItem):
    name = 'Lantern (hooded)'
    base_cost = '5 gp'
    base_weight = 2


class Lock(CommonItem):
    name = 'Lock'
    base_cost = '10 gp'
    base_weight = 1


class LoreBook(CommonItem):
    name = 'Book of Lore'
    base_cost = '30 gp'
    base_weight = 5


class MagnifyingGlass(CommonItem):
    name = 'Magnifying Glass'
    base_cost = '100 gp'
    base_weight = 0


class Manacles(CommonItem):
    name = 'Manacles'
    base_cost = '2 gp'
    base_weight = 6


class MessKit(CommonItem):
    name = 'Mess Kit'
    base_cost = '2 sp'
    base_weight = 1


class PrayerBook(CommonItem):
    name = 'Prayer Book'
    base_cost = '5 sp'
    base_weight = 2


class SteelMirror(CommonItem):
    name = 'Mirror (steel)'
    base_cost = '5 gp'
    base_weight = 0.5


class OilFlask(CommonItem):
    name = 'Oil (flask)'
    base_cost = '1 sp'
    base_weight = 1


class PaperSheet(CommonItem):
    name = 'Paper (one sheet)'
    base_cost = '2 sp'
    base_weight = 0


class Parchment(CommonItem):
    name = 'Parchment (one sheet)'
    base_cost = '1 sp'
    base_weight = 0


class Perfume(CommonItem):
    name = 'Perfume (vial)'
    base_cost = '5 gp'
    base_weight = 0


class MinersPick(CommonItem):
    name = 'Pick (miner\'s)'
    base_cost = '2 gp'
    base_weight = 10


class Piton(CommonItem):
    name = 'Piton'
    base_cost = '5 cp'
    base_weight = 0.25


class BasicPoison(CommonItem):
    name = 'Poison (basic; vial)'
    base_cost = '100 gp'
    base_weight = 0


class Pole(CommonItem):
    name = 'Pole (10 foot)'
    base_cost = '5 cp'
    base_weight = 7


class HealingPotion(CommonItem):
    name = 'Potion of Healing'
    base_cost = '50 gp'
    base_weight = 0.5


class Quiver(CommonItem):
    name = 'Quiver'
    base_cost = '1 gp'
    base_weight = 1


class PortableRam(CommonItem):
    name = 'Ram (portable)'
    base_cost = '4 gp'
    base_weight = 35


class Rations(CommonItem):
    name = 'Rations (1 day)'
    base_cost = '5 sp'
    base_weight = 2


class Robes(CommonItem):
    name = 'Robes'
    base_cost = '1 gp'
    base_weight = 4


class HempenRope(CommonItem):
    name = 'Rope (hempen; 50 feet)'
    base_cost = '1 gp'
    base_weight = 10


class LittleSandbag(CommonItem):
    name = 'Little bag of sand'
    base_cost = '2 sp'
    base_weight = 0.5


class SilkRope(CommonItem):
    name = 'Rope (silk; 50 feet)'
    base_cost = '10 gp'
    base_weight = 5


class Tinderbox(CommonItem):
    name = 'Tinderbox'
    base_cost = '5 sp'
    base_weight = 1


class MerchantsScale(CommonItem):
    name = 'Scale (merchant\'s)'
    base_cost = '5 gp'
    base_weight = 3


class SealingWax(CommonItem):
    name = 'Sealing Wax'
    base_cost = '5 sp'
    base_weight = 0


class Shovel(CommonItem):
    name = 'Shovel'
    base_cost = '2 gp'
    base_weight = 5


class SignalWhistle(CommonItem):
    name = 'Signal Whistle'
    base_cost = '5 cp'
    base_weight = 0


class SignetRing(CommonItem):
    name = 'Signet Ring'
    base_cost = '5 gp'
    base_weight = 0


class SmallKnife(CommonItem):
    name = 'Small Knife (non-weapon)'
    base_cost = '2 gp'
    base_weight = 1
    

class Soap(CommonItem):
    name = 'Soap'
    base_cost = '2 cp'
    base_weight = 1


class Spellbook(CommonItem):
    name = 'Spellbook'
    base_cost = '50 gp'
    base_weight = 3


class IronSpikes(CommonItem):
    name = 'Spikes (iron; x10)'
    base_cost = '1 gp'
    base_weight = 5


class Spyglass(CommonItem):
    name = 'Spyglass'
    base_cost = '1000 gp'
    base_weight = 1


class Tent(CommonItem):
    name = 'Tent (two-person)'
    base_cost = '2 gp'
    base_weight = 20


class Torch(CommonItem):
    name = 'Torch'
    base_cost = '1 cp'
    base_weight = 1


class String(CommonItem):
    name = 'String (10 feet)'
    base_cost = '2 cp'
    base_weight = 0


class Vestments(CommonItem):
    name = 'Vestments'
    base_cost = '10 gp'
    base_weight = 4


class Whetstone(CommonItem):
    name = 'Whetstone'
    base_cost = '1 cp'
    base_weight = 1