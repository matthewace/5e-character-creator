class Morality:
    """Generic class for Morality to be sub-classed."""
    name = str


class GoodMorality(Morality):
    name = "Good"


class NeutralMorality(Morality):
    name = "Neutral"


class EvilMorality(Morality):
    name = "Evil"