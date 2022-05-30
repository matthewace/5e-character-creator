from .background import (
    Acolyte, Background, Charlatan, Criminal, Entertainer, Gladiator, FolkHero, 
    GuildArtisan, GuildMerchant, Hermit, Noble, Knight, Outlander, Sage,
    Sailor, Pirate, Soldier, Spy, Urchin)


__all__ = [
    'Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Gladiator', 'FolkHero',
    'GuildArtisan', 'GuildMerchant', 'Hermit', 'Noble', 'Knight', 'Outlander',
    'Sage', 'Sailor', 'Pirate', 'Soldier', 'Spy', 'Urchin'
]

BACKGROUND_MAP = {
    'acolyte': Acolyte,
    'charlatan': Charlatan,
    'criminal': Criminal,
    'entertainer': Entertainer,
    'folkhero': FolkHero,
    'gladiator': Gladiator,
    'guildartisan': GuildArtisan,
    'guildmerchant': GuildMerchant,
    'hermit': Hermit,
    'knight': Knight,
    'noble': Noble,
    'outlander': Outlander,
    'pirate': Pirate,
    'sage': Sage,
    'sailor': Sailor,
    'soldier': Soldier,
    'spy': Spy,
    'urchin': Urchin,
}