from typing import List, Tuple

class CharacterClass:
    """Generic class to be sub-classed"""
    name = str
    hit_die = str
    armor_proficiencies = List[str]
    tool_proficiencies = List[str]
    weapon_proficiencies = List[str]
    saving_throws = List[str]
    skills = List[str]
    equipment = List[object]
    level = List[List[Tuple[str, object]]]