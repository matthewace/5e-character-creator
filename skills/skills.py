"""Module to track the various Skills available in 5e.  This is basically just
to help store the base stat used and to help track in which skills a Character3
is proficient.

Using the standard Skills from 5e Character Sheet:
    Acrobatics, Animal Handling, Arcana, Athletics, Deception, History,
    Insight, Intimidation, Investigation, Medicine, Nature, Perception,
    Performance, Persuasion, Religion, Sleight of Hand, Stealth, Survival
"""


class Skill:
    """Base Skill Class to be sub-classed"""
    name = str
    ability = str


class Acrobatics(Skill):
    name = 'Acrobatics'
    ability = 'DEX'


class AnimalHandling(Skill):
    name = 'Animal Handling'
    ability = 'WIS'


class Arcana(Skill):
    name = 'Arcana'
    ability = 'INT'


class Athletics(Skill):
	name = 'Athletics'
	ability = 'STR'


class Deception(Skill):
	name = 'Deception'
	ability = 'CHA'


class History(Skill):
	name = 'History'
	ability = 'INT'


class Insight(Skill):
	name = 'Insight'
	ability = 'WIS'


class Intimidation(Skill):
	name = 'Intimidation'
	ability = 'CHA'


class Investigation(Skill):
	name = 'Investigation'
	ability = 'INT'


class Medicine(Skill):
	name = 'Medicine'
	ability = 'WIS'


class Nature(Skill):
	name = 'Nature'
	ability = 'INT'


class Perception(Skill):
	name = 'Perception'
	ability = 'WIS'


class Performance(Skill):
	name = 'Performance'
	ability = 'CHA'


class Persuasion(Skill):
	name = 'Persuasion'
	ability = 'CHA'


class Religion(Skill):
	name = 'Religion'
	ability = 'INT'


class SleightOfHand(Skill):
	name = 'Sleight of Hand'
	ability = 'DEX'


class Stealth(Skill):
	name = 'Stealth'
	ability = 'DEX'


class Survival(Skill):
    name = 'Survival'
    ability = 'WIS'