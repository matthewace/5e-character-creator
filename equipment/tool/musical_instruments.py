"""Musical Instruments in DnD 5e.

    Bagpipes, Drum, Dulcimer, Flute, Lute, Lyre, Horn, PanFlute, Shawm, Viol
"""


from dnd.equipment.base_equipment import Tool


class MusicalInstrument(Tool):
    """Base class for Musical Instruments"""
    item_type = 'Musical Instrument'


class Bagpipes(MusicalInstrument):
    name = 'Bagpipes'
    base_cost = '30 gp'
    base_weight = 6


class Drum(MusicalInstrument):
    name = 'Drum'
    base_cost = '6 gp'
    base_weight = 3


class Dulcimer(MusicalInstrument):
    name = 'Dulcimer'
    base_cost = '25 gp'
    base_weight = 10


class Flute(MusicalInstrument):
    name = 'Flute'
    base_cost = '2 gp'
    base_weight = 1


class Lute(MusicalInstrument):
    name = 'Lute'
    base_cost = '35 gp'
    base_weight = 2


class Lyre(MusicalInstrument):
    name = 'Lyre'
    base_cost = '30 gp'
    base_weight = 2


class Horn(MusicalInstrument):
    name = 'Horn'
    base_cost = '3 gp'
    base_weight = 2


class PanFlute(MusicalInstrument):
    name = 'Pan-Flute'
    base_cost = '12 gp'
    base_weight = 2
    
    
class Shawm(MusicalInstrument):
    name = 'Shawm'
    base_cost = '2 gp'
    base_weight = 1


class Viol(MusicalInstrument):
    name = 'Viol'
    base_cost = '30 gp'
    base_weight = 1