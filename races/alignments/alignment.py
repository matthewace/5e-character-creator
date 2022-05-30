class Attitude:
    """Generic class for Attitude to be sub-classed."""
    name = str


class LawfulAttitude(Attitude):
    name = "Lawful"


class NeutralAttitude(Attitude):
    name = "Neutral"


class ChaoticAttitude(Attitude):
    name = "Chaotic"


class Morality:
    """Generic class for Morality to be sub-classed."""
    name = str


class GoodMorality(Morality):
    name = "Good"


class NeutralMorality(Morality):
    name = "Neutral"


class EvilMorality(Morality):
    name = "Evil"



class Alignment:
    """Generic Alignment class to be sub-classed."""
    name = str
    short_name = str
    attitude = Attitude
    morality = Morality


class LawfulGood(Alignment):
    name = "Lawful Good"
    short_name = "LG"
    attitude = LawfulAttitude
    morality = GoodMorality


class LawfulNeutral(Alignment):
    name = "Lawful Neutral"
    short_name = "LN"
    attitude = LawfulAttitude
    morality = NeutralMorality


class LawfulEvil(Alignment):
    name = "Lawful Evil"
    short_name = "LE"
    attitude = LawfulAttitude
    morality = EvilMorality


class NeutralGood(Alignment):
    name = "Neutral Good"
    short_name = "NG"
    attitude = NeutralAttitude
    morality = GoodMorality


class TrueNeutral(Alignment):
    name = "True Neutral"
    short_name = "NN"
    attitude = NeutralAttitude
    morality = NeutralMorality


class NeutralEvil(Alignment):
    name = "Neutral Evil"
    short_name = "NE"
    attitude = NeutralAttitude
    morality = EvilMorality


class ChaoticGood(Alignment):
    name = "Chaotic Good"
    short_name = "CG"
    attitude = ChaoticAttitude
    morality = GoodMorality


class ChaoticNeutral(Alignment):
    name = "Chaotic Neutral"
    short_name = "CN"
    attitude = ChaoticAttitude
    morality = NeutralMorality


class ChaoticEvil(Alignment):
    name = "Chaotic Evil"
    short_name = "CE"
    attitude = ChaoticAttitude
    morality = EvilMorality


class Unaligned(Alignment):
    name = "Unaligned"
    short_name = "UA"
    attitude = None
    morality = None