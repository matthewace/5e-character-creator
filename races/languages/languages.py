"""Module for Languages in the world of 5e

Standard:
    Common, Dwarvish, Elvish, Giant, Gnomish, Goblin, Halfling, Orcish
Exotic:
    Abyssal, Celestial, Draconic, Deep Speech, Infernal, Primordial,
    Sylvan, Undercommon
"""


class Language:
    """Generic Language to be sub-classed"""
    name = str
    script = str


class Common(Language):
    name = "Common"
    script = "Common"


class Dwarvish(Language):
    name = "Dwarvish"
    script = "Dwarvish"


class Elvish(Language):
    name = "Elvish"
    script = "Elvish"


class Giant(Language):
    name = "Giant"
    script = "Dwarvish"


class Gnomish(Language):
    name = "Gnomish"
    script = "Dwarvish"


class Goblin(Language):
    name = "Goblin"
    script = "Dwarvish"


class HalflingLang(Language):
    name = "Halfling"
    script = "Common"


class Orc(Language):
    name = "Orcish"
    script = "Dwarvish"


class Abyssal(Language):
    name = "Abyssal"
    script = "Infernal"


class Celestial(Language):
    name = "Celestial"
    script = "Celestial"


class Draconic(Language):
    name = "Draconic"
    script = "Draconic"


class DeepSpeech(Language):
    name = "Deep Speech"
    script = ""


class Infernal(Language):
    name = "Infernal"
    script = "Infernal"


class Primordial(Language):
    name = "Primordial"
    script = "Dwarvish"


class Sylvan(Language):
    name = "Sylvan"
    script = "Elvish"


class Undercommon(Language):
    name = "Undercommon"
    script = "Elvish"