import os
import random

from .alignment import (LawfulGood, LawfulNeutral, LawfulEvil,
                       NeutralGood, TrueNeutral, NeutralEvil,
                       ChaoticGood, ChaoticNeutral, ChaoticEvil,
                       Unaligned, Alignment,)

__all__ = [
    'LawfulGood', 'LawfulNeutral', 'LawfulEvil',
    'NeutralGood', 'TrueNeutral', 'NeutralEvil',
    'ChaoticGood', 'ChaoticNeutral', 'ChaoticEvil',
    'Unaligned',
]

ALIGNMENT_MAP = {
    'lawfulgood': LawfulGood,
    'lawfulneutral': LawfulNeutral,
    'lawfulevil': LawfulEvil,
    'neutralgood': NeutralGood,
    'trueneutral': TrueNeutral,
    'neutralevil': NeutralEvil,
    'chaoticgood': ChaoticGood,
    'chaoticneutral': ChaoticNeutral,
    'chaoticevil': ChaoticEvil,
    'unaligned': Unaligned,
}