from typing import Dict, List, Tuple


class CharacterRace:
    """Generic class to be sub-classed by main Races
    
    Attributes:
    -----------
    name : str
        Common name of Race
    base_speed : int
        Walking speed
    base_height : int
        Height, in inches, before modifiers
    height_mod : str
        Dice modifier e.g. `2d6`
    base_weight : int
        Weight, in lbs, before modifiers
    weight_mod : str
        Dice modifier e.g. `1d4`
    size : sizes.Size
        How big the creature is on a game grid
    languages : List[languages.Language]
        Known languages
    alignments : List[alignments.Alignment]
        Possible alignments
    male_names : List[str]
        Typical Male names of creatures
    female_names : List[str]
        Typical Female names of creatures
    clan_names : List[str]
        Typical Clan names of creatures
    level : List[Dict[str, object]]
        List of actions to take at each level
    """
    name = str
    base_speed = int
    base_height = int
    height_mod = str
    base_weight = int
    weight_mod = str
    size = str
    languages = List[str]
    alignments = List[str]
    male_names = List[str]
    female_name = List[str]
    clan_names = List[str]
    traits = List[Tuple[str, object]]