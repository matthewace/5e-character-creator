from .packs import (
    BurglarsPack, DiplomatsPack, DungeoneersPack, EntertainersPack,
    ExplorersPack, PriestsPack, ScholarsPack
)

__all__ = [
    'BurglarsPack', 'DiplomatsPack', 'DungeoneersPack', 'EntertainersPack',
    'ExplorersPack', 'PriestsPack', 'ScholarsPack'
]

PACK_MAP = {
    'burglarspack': BurglarsPack,
    'diplomatspack': DiplomatsPack,
    'dungeoneerspack': DungeoneersPack,
    'entertainerspack': EntertainersPack,
    'explorerspack': ExplorersPack,
    'priestspack': PriestsPack,
    'scholarspack': ScholarsPack,
}


class PackHandler:
    """Handler for all Equipment Packs"""
    pass