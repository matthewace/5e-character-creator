class Attitude:
    """Generic class for Attitude to be sub-classed."""
    name = str


class LawfulAttitude(Attitude):
    name = "Lawful"


class NeutralAttitude(Attitude):
    name = "Neutral"


class ChaoticAttitude(Attitude):
    name = "Chaotic"