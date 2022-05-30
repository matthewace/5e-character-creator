"""Module for various Equipment Packs in DnD 5e.

    BurglarsPack, DiplomatsPack, DungeoneersPack, EntertainersPack,
    ExplorersPack, PriestsPack, ScholarsPack

    Each pack contains a collection of adventuring gear.
"""

from dnd.equipment.base_equipment import EquipmentPack
from dnd.equipment.gear import *
from dnd.equipment.tool import *


class BurglarsPack(EquipmentPack):
    name = 'Burglar\'s Pack'
    base_cost = '16 gp'
    base_weight = 43.5
    base_contents = {
        Backpack: 1,
        BallBearings: 1,
        String: 1,
        Bell: 1,
        Candle: 5,
        Crowbar: 1,
        Hammer: 1,
        Piton: 10,
        HoodedLantern: 1,
        OilFlask: 2,
        Rations: 5,
        Tinderbox: 1,
        Waterskin: 1,
        HempenRope: 1
    }
    

class DiplomatsPack(EquipmentPack):
    name = 'Diplomat\'s Pack'
    base_cost = '39 gp'
    base_weight = 41
    base_contents = {
        Chest: 1,
        ScrollCase: 2,
        FineClothes: 1,
        InkBottle: 1,
        InkPen: 1,
        Lamp: 1,
        OilFlask: 2,
        PaperSheet: 5,
        Perfume: 1,
        SealingWax: 1,
        Soap: 1
    }


class DungeoneersPack(EquipmentPack):
    name = 'Dungeoneer\'s Pack'
    base_cost = '12 gp'
    base_weight = 57.5
    base_contents = {
        Backpack: 1,
        Crowbar: 1,
        Hammer: 1,
        Piton: 10,
        Torch: 10,
        Tinderbox: 1,
        Rations: 10,
        Waterskin: 1,
        HempenRope: 1
    }


class EntertainersPack(EquipmentPack):
    name = 'Entertainer\'s Pack'
    base_cost = '40 gp'
    base_weight = 32
    base_contents = {
        Backpack: 1,
        Bedroll: 1,
        CostumeClothes: 2,
        Candle: 5,
        Rations: 5,
        Waterskin: 1,
        DisguiseKit: 1
    }


class ExplorersPack(EquipmentPack):
    name = 'Explorer\'s Pack'
    base_cost = '10 gp'
    base_weight = 55
    base_contents = {
        Backpack: 1,
        Bedroll: 1,
        MessKit: 1,
        Tinderbox: 1,
        Torch: 10,
        Rations: 10,
        Waterskin: 1,
        HempenRope: 1
    }


class PriestsPack(EquipmentPack):
    name = 'Priest\'s Pack'
    base_cost = '19 gp'
    base_weight = 18
    base_contents = {
        Backpack: 1,
        Blanket: 1,
        Candle: 10,
        Tinderbox: 1,
        AlmsBox: 1,
        Incense: 2,
        Censer: 1,
        Vestments: 1,
        Rations: 2,
        Waterskin: 1
    }


class ScholarsPack(EquipmentPack):
    name = 'Scholar\'s Pack'
    base_cost = '40 gp'
    base_weight = 15.5
    base_contents = {
        Backpack: 1,
        LoreBook: 1,
        InkBottle: 1,
        InkPen: 1,
        Parchment: 10,
        LittleSandbag: 1,
        SmallKnife: 1
    }