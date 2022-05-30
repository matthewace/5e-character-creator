"""Module for Spells

http://dnd5e.wikidot.com/spells
https://roll20.net/compendium/dnd5e/Spells%20List#content
https://donjon.bin.sh/5e/spells/
https://www.dnd-spells.com/spells

There are quite a few ways to classify spells: level, class, school, etc...

Currently have all lvl 0 and lvl 1 spell (and one lvl2) from PHB.
"""
from typing import List

from dnd import classes


class Spell:
    """Base class for Spells... I imagine this is going to go through many
    iterations...

    This might end up being classified as Equipment or even a Weapon sub-class.

    Attributes
    ----------
    name : str
        The name of the spell.
    description : str
        A detailed description of the spell.
    character_class : List[classes.CharacterClass]
        List of Character classes this spell can be used with.
    level : int
        The level of the spell.  Cantrips are lvl 0.
    cast_range : int
        Distance in feet the spell can be cast.  Touch spells are 0 cast_range,
        and Self spells are -1 cast_range
    school : str
        Which school is the spell from e.g. `Transmutation` or `Illusion.`
    ritual : bool
        Whether or not the spell is a ritual
    casting_time : str
        Length of time to cast the spell.
    duration : int
        How long, in seconds, the spell stays active.  0 indicates the spell
        is over instantaneously, for example using Fire Bolt.  One round is
        equal to 6 seconds.
    components : str
        Which components are required to cast the spell.  Options are Verbal,
        Somatic, Material, and Cost.  Denoted as a string e.g. `VS` or `SMgp`.
    concentration : bool
        Whether concentration needs to be sustained to keep spell active.
    """
    name = str
    description = str
    character_class = List[classes.CharacterClass]
    level = int
    cast_range = int
    school = str
    ritual = bool
    casting_time = str
    duration = str
    components = str
    concentration = bool


class AcidSplash(Spell):
    name = 'Acid Splash'
    description = """
You hurl a bubble of acid. Choose one creature within range, or choose two 
creatures within range that are within 5 feet of each other. A target must 
succeed on a Dexterity saving throw or take 1d6 acid damage.
    """.strip()
    character_class = [classes.Sorcerer, classes.Wizard]
    level = 0
    cast_range = 60
    school = 'Conjuration'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class BladeWard(Spell):
    name = 'Blade Ward'
    description = """
You extend your hand and trace a sigil of warding in the air. Until the end of 
your next turn, you have resistance against bludgeoning, piercing, and 
slashing damage dealt by weapon attacks.
    """.strip()
    character_class = [classes.Bard, classes.Sorcerer,
                       classes.Warlock, classes.Wizard]
    level = 0
    cast_range = -1
    school = 'Abjuration'
    ritual = False
    casting_time = '1 round'
    duration = 0
    components = 'VS'
    concentration = False


class ChillTouch(Spell):
    name = 'Chill Touch'
    description = """
You create a ghostly, skeletal hand in the space of a creature within range.
Make a ranged spell attack against the creature to assail it with the chill of
the grave. On a hit, the target takes 1d8 necrotic damage, and it can’t regain
hit points until the start of your next turn. Until then, the hand clings to
the target. If you hit an undead target, it also has disadvantage on attack
rolls against you until the end of your next turn. 

~~~ At higher level ~~~
This spell’s damage increases by 1d8 when you reach 5th level (2d8), 11th level
(3d8), and 17th level (4d8).
    """.strip()
    character_class = [classes.Sorcerer, classes.Warlock, classes.Wizard]
    level = 0
    cast_range = 120
    school = 'Necromancy'
    ritual = False
    casting_time = '1 action'
    duration = 6
    components = 'VS'
    concentration = False


class DancingLights(Spell):
    name = 'Dancing Lights'
    description = """
You create up to four torch-sized lights within range, making them appear as
torches, lanterns, or glowing orbs that hover in the air for the duration.
You can also combine the four lights into one glowing vaguely humanoid form of
Medium size. Whichever form you choose, each light sheds dim light in a 10-foot
radius.

As a bonus action on your turn, you can move the lights up to 60 feet to a new
spot within range. A light must be within 20 feet of another light created by
this spell, and a light winks out if it exceeds the spell’s range.
    """.strip()
    character_class = [classes.Bard, classes.Sorcerer, classes.Wizard]
    level = 0
    cast_range = 120
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'VSM (a bit of phosphorous or wychwood, or a glowworm'
    concentration = True


class Druidcraft(Spell):
    name = 'Druidcraft'
    description = """
Whispering to the spirits of nature, you create one of the following effects
within range:

• You create a tiny, harmless sensory effect that predicts what the weather
will be at your location for the next 24 hours. The effect might manifest as a
golden orb  for clear skies, a cloud for rain, falling snowflakes for snow, and
so on. This effect persists for 1 round.
• You instantly make a flower blossom, a seed pod open, or a leaf bud bloom.
• You create an instantaneous, harmless sensory effect, such as falling leaves,
a puff of wind, the sound of a small animal, or the faint odor of skunk. The
effect  must fit in a 5-foot cube.
• You instantly light or snuff out a candle, a torch, or a small campfire.
    """.strip()
    character_class = [classes.Druid]
    level = 0
    cast_range = 30
    school = 'Transmutation'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class EldritchBlast(Spell):
    name = 'Eldritch Blast'
    description = """
A beam of crackling energy streaks toward a creature within range. Make a
ranged spell attack against the target. On a hit, the target takes 1d10 force
damage. 

~~~ At higher level ~~~
The spell creates more than one beam when you reach higher levels:
    Two beams at 5th level
    Three beams at 11th level
    Four beams at 17th level.
You can direct the beams at the same target or at different ones. Make a
separate attack roll for each beam.
    """.strip()
    character_class = [classes.Warlock]
    level = 0
    cast_range = 120
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class Firebolt(Spell):
    name = 'Fire Bolt'
    description = """
You hurl a mote of fire at a creature or object within range. Make a ranged
spell attack against the target. On a hit, the target takes 1d10 fire damage. A
flammable object hit by this spell ignites if it isn’t being worn or carried.

~~~ At higher level ~~~
This spell’s damage increases by 1d10 when you reach 5th level (2d10), 11th
level (3d10), and 17th level (4d10).
    """.strip()
    character_class = [classes.Sorcerer, classes.Wizard]
    level = 0
    cast_range = 120
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class Friends(Spell):
    name = 'Friends'
    description = """
For the duration, you have advantage on all Charisma checks directed at one
creature of your choice that isn’t hostile toward you. When the spell ends, the
creature realizes that you used magic to influence its mood and becomes hostile
toward you. A creature prone to violence might attack you. Another creature
might seek retribution in other ways (at the DM’s discretion), depending on the
nature of your interaction with it.
    """.strip()
    character_class = [
        classes.Bard, classes.Sorcerer, classes.Warlock, classes.Wizard
    ]
    level = 0
    cast_range = -1
    school = 'Enchantment'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'SM (a small amount of makeup applied to the face as this ' +\
                 'as this spell is cast)'
    concentration = True


class Guidance(Spell):
    name = 'Guidance'
    description = """
You touch one willing creature. Once before the spell ends, the target can roll
a d4 and add the number rolled to one ability check of its choice. It can roll
the die before or after making the ability check. The spell then ends.
    """.strip()
    character_class = [classes.Cleric, classes.Druid]
    level = 0
    cast_range = 0
    school = 'Divination'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'VS'
    concentration = True


class Light(Spell):
    name = 'Light'
    description = """
You touch one object that is no larger than 10 feet in any dimension. Until the
spell ends, the object sheds bright light in a 20-foot radius and dim light for
an additional 20 feet. The light can be colored as you like. Completely
covering the object with something opaque blocks the light. The spell ends if
you cast it again or dismiss it as an action.

If you target an object held or worn by a hostile creature, that creature must
succeed on a Dexterity saving throw to avoid the spell.
    """.strip()
    character_class = [
        classes.Bard, classes.Cleric, classes.Sorcerer, classes.Wizard
    ]
    level = 0
    cast_range = 0
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 60 * 60
    components = 'VM (a firefly or phosphorescent moss)'
    concentration = False


class MageHand(Spell):
    name = 'Mage Hand'
    description = """
A spectral, floating hand appears at a point you choose within range.
The hand lasts for the duration or until you dismiss it as an action. The hand
vanishes if it is ever more than 30 feet away from you or if you cast this
spell again.

You can use your action to control the hand. You can use the hand to manipulate
an object, open an unlocked door or container, stow or retrieve an item from an
open container, or pour the contents out of a vial. You can move the hand up to
30 feet each time you use it.

The hand can’t attack, activate magical items, or carry more than 10 pounds.
    """.strip()
    character_class = [
        classes.Bard, classes.Sorcerer, classes.Warlock, classes.Wizard
    ]
    level = 0
    cast_range = 30
    school = 'Conjuration'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'VS'
    concentration = False


class Mending(Spell):
    name = 'Mending'
    description = """
This spell repairs a single break or tear in an object you touch, such as
broken chain link, two halves of a broken key, a torn cloack, or a leaking
wineskin.
As long as the break or tear is no larger than 1 foot in any dimension, you
mend it, leaving no trace of the former damage.

This spell can physically repair a magic item or construct, but the spell can’t
restore magic to such an object.
    """.strip()
    character_class = [
        classes.Bard, classes.Cleric, classes.Druid, classes.Sorcerer,
        classes.Wizard
    ]
    level = 0
    cast_range = 0
    school = 'Transmutation'
    ritual = False
    casting_time = '1 minute'
    duration = 0
    components = 'VSM (two lodestones)'
    concentration = False


class Message(Spell):
    name = 'Message'
    description = """
You point your finger toward a creature within range and whisper a message.
The target (and only the target) hears the message and can reply in a whisper
that only you can hear.

You can cast this spell through solid objects if you are familiar with the
target and know it is beyond the barrier. Magical silence, 1 foot of stone, 1
inch of common metal, a thin sheet of lead, or 3 feet of wood blocks the spell.
The spell doesn’t have to follow a straight line and can travel freely around
corners or through openings.
    """.strip()
    character_class = [classes.Bard, classes.Sorcerer, classes.Wizard]
    level = 0
    cast_range = 120
    school = 'Transmutation'
    ritual = False
    casting_time = '1 action'
    duration = 6
    components = 'VSM (a short piece of copper wire)'
    concentration = False


class MinorIllusion(Spell):
    name = 'Minor Illusion'
    description = """
You create a sound or an image of an object within range that lasts for the
duration. The illusion also ends if you dismiss it as an action or cast this
spell again.

If you create a sound, its volume can range from a whisper to a scream. It can
be your voice, someone else’s voice, a lion’s roar, a beating of drums, or any
other sound you choose. The sound continues unabated throughout the duration,
or you can make discrete sounds at different times before the spell ends.

If you create an image of an object such as a chair, muddy footprints, or a
small chest it must be no larger than a 5-foot cube. The image can’t create
sound, light, smell, or any other sensory effect. Physical interaction with the
image reveals it to be an illusion, because things can pass through it.

If a creature uses its action to examine the sound or image, the creature can
determine that it is an illusion with a successful Intelligence (Investigation)
check against your spell save DC. If a creature discerns the illusion for what
it is, the illusion becomes faint to the creature.
    """.strip()
    character_class = [
        classes.Bard, classes.Sorcerer, classes.Warlock, classes.Wizard]
    level = 0
    cast_range = 30
    school = 'Illusion'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'SM (a bit of fleece)'
    concentration = False


class PoisonSpray(Spell):
    name = 'Poison Spray'
    description = """
You extend your hand toward a creature you can see within range and project a
puff of noxious gas from your palm. The creature must succeed on a Constitution
saving throw or take 1d12 poison damage.

~~~ At higher level ~~~
This spell’s damage increases by 1d12 when you reach 5th level (2d12), 11th
level (3d12), 17th level (4d12).
    """.strip()
    character_class = [
        classes.Druid, classes.Sorcerer, classes.Warlock, classes.Wizard]
    level = 0
    cast_range = 10
    school = 'Conjuration'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class Prestidigitation(Spell):
    name = 'Prestidigitation'
    description = """
This spell is a minor magical trick that novice spellcasters use for practice.
You create one of the following magical effects within range:
    • You create an instantaneous, harmless sensory effect, such as a shower of
    sparks, a puff of wind, faint musical notes, or an odd odor.
    • You instantaneously light or snuff out a candle, a torch, or a small
    campfire.
    • You instantaneously clean or soil an object no larger than 1 cubic foot.
    • You chill, warm, or flavor up to 1 cubic foot of nonliving material for 1
    hour.
    • You make a color, a small mark, or a symbol appear on an object or a
    surface for 1 hour.
    • You create a nonmagical trinket or an illusory image that can fit in your
    hand and that lasts until the end of your next turn.
If you cast this spell multiple times, you can have up to three of its
non-instantaneous effects active at a time, and you can dismiss such an effect
as an action.
    """.strip()
    character_class = [
        classes.Bard, classes.Sorcerer, classes.Warlock, classes.Wizard]
    level = 0
    cast_range = 10
    school = 'Transmutation'
    ritual = False
    casting_time = '1 action'
    duration = 60 * 60
    components = 'VS'
    concentration = False


class ProduceFlame(Spell):
    name = 'Produce Flame'
    description = """
A flickering flame appears in your hand.
The flame remains there for the duration and harms neither you nor your
equipment. The flame sheds bright light in a 10-foot radius and dim light for
an additional 10 feet. The spell ends if you dismiss it as an action or if you
cast it again.

You can also attack with the flame, although doing so ends the spell. When you
cast this spell, or as an action on a later turn, you can hurl the flame at a
creature within 30 feet of you. Make a ranged spell attack. On a hit, the
target takes 1d8 fire damage.

~~~ At higher level ~~~
This spell’s damage increases by 1d8 when you reach 5th level (2d8), 11th level
(3d8), and 17th level (4d8).
    """.strip()
    character_class = [classes.Druid]
    level = 0
    cast_range = -1
    school = 'Conjuration'
    ritual = False
    casting_time = '1 action'
    duration = 10 * 60
    components = 'VS'
    concentration = False


class RayOfFrost(Spell):
    name = 'Ray of Frost'
    description = """
A frigid beam of blue-white light streaks toward a creature within range. Make
a ranged spell attack against the target. On a hit, it takes 1d8 cold damage,
and its speed is reduced by 10 feet until the start of your next turn.

~~~ At higher level ~~~
The spell’s damage increases by 1d8 when you reach 5th level (2d8), 11th level
(3d8), and 17th level (4d8).
    """.strip()
    character_class = [classes.Sorcerer, classes.Wizard]
    level = 0
    cast_range = 60
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class Resistance(Spell):
    name = 'Resistance'
    description = """
You touch one willing creature. Once before the spell ends, the target can roll
a d4 and add the number rolled to one saving throw of its choice. It can roll
the die before or after the saving throw. The spell then ends.
    """.strip()
    character_class = [classes.Cleric, classes.Druid]
    level = 0
    cast_range = 0
    school = 'Abjuration'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'VSM (a miniature cloak)'
    concentration = True


class SacredFlame(Spell):
    name = 'Sacred Flame'
    description = """
Flame-like radiance descends on a creature that you can see within range. The
target must succeed on a Dexterity saving throw or take 1d8 radiant damage. The
target gains no benefit from cover for this saving throw. 

~~~ At higher level ~~~
The spell’s damage increases by 1d8 when you reach 5th level (2d8), 11th level
(3d8), and 17th level (4d8).
    """.strip()
    character_class = [classes.Cleric]
    level = 0
    cast_range = 60
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class Shillelagh(Spell):
    name = 'Shillelagh'
    description = """
The wood of a club or quarterstaff you are holding is imbued with nature’s
power.
For the duration, you can use your spellcasting ability instead of Strength for
the attack and damage rolls of melee attacks using that weapon, and the
weapon’s damage die becomes a d8. The weapon also becomes magical, if it isn’t
already. The spell ends if you cast it again or if you let go of the weapon.
    """.strip()
    character_class = [classes.Druid]
    level = 0
    cast_range = 0
    school = 'Transmutation'
    ritual = False
    casting_time = '1 bonus action'
    duration = 60
    components = 'VSM (mistletoe, a shamrock leaf, and a club or quarterstaff)'
    concentration = False


class ShockingGrasp(Spell):
    name = 'Shocking Grasp'
    description = """
Lightning springs from your hand to deliver a shock to a creature you try to
touch.
Make a melee spell attack against the target. You have advantage on the attack
roll if the target is wearing armor made of metal. On a hit, the target takes
1d8 lightning damage, and it can’t take reactions until the start of its next
turn.
    """.strip()
    character_class = [classes.Sorcerer, classes.Wizard]
    level = 0
    cast_range = 0
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class SpareTheDying(Spell):
    name = 'Spare the Dying'
    description = """
You touch a living creature that has 0 hit points. The creature becomes stable.
This spell has no effect on undead or constructs.
    """.strip()
    character_class = [classes.Cleric]
    level = 0
    cast_range = 0
    school = 'Necromancy'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class Thaumaturgy(Spell):
    name = 'Thaumaturgy'
    description = """
You manifest a minor wonder, a sign of supernatural power, within range. You
create one of the following magical effects within range:

    • Your voice booms up to three times as loud as normal for 1 minute.
    • You cause flames to flicker, brighten, dim, or change color for 1 minute.
    • You cause harmless tremors in the ground for 1 minute.
    • You create an instantaneous sound that originates from a point of your
    choice within range, such as a rumble of thunder, the cry of a raven, or
    ominous whispers.
    • You instantaneously cause an unlocked door or window to fly open or slam
    shut.
    • You alter the appearance of your eyes for 1 minute.

If you cast this spell multiple times, you can have up to three of its 1-minute
effects active at a time, and you can dismiss such an effect as an action.
    """.strip()
    character_class = [classes.Cleric]
    level = 0
    cast_range = 30
    school = 'Transmutation'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'V'
    concentration = False


class ThornWhip(Spell):
    name = 'Thorn Whipo'
    description = """
You create a long, vine-like whip covered in thorns that lashes out at your
command toward a creature in range. Make a melee spell attack against the
target. If the attack hits, the creature takes 1d6 piercing damage, and if the
creature is Large or smaller, you pull the creature up to 10 feet closer to
you.

~~~ At higher level ~~~
This spell’s damage increases by 1d6 when you reach 5th level (2d6), 11th level
(3d6), and 17th level (4d6).
    """.strip()
    character_class = [classes.Druid]
    level = 0
    cast_range = 30
    school = 'Transmutation'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VSM (the stem of a plant with thorns)'
    concentration = False


class TrueStrike(Spell):
    name = 'True Strike'
    description = """
You extend your hand and point a finger at a target in range. Your magic grants
you a brief insight into the target’s defenses. On your next turn, you gain
advantage on your first attack roll against the target, provided that this
spell hasn’t ended.
    """.strip()
    character_class = [
        classes.Bard, classes.Sorcerer, classes.Warlock, classes.Wizard]
    level = 0
    cast_range = 30
    school = 'Divination'
    ritual = False
    casting_time = '1 action'
    duration = 6
    components = 'S'
    concentration = True


class ViciousMockery(Spell):
    name = 'Vicious Mockery'
    description = """
You unleash a string of insults laced with subtle enchantments at a creature
you can see within range.
If the target can hear you (thought it need not understand you), it must
succeed on a Wisdom saving throw or take 1d4 psychic damage and have
disadvantage on the next attack roll it makes before the end of its next turn.

~~~ At higher level ~~~
This spell’s damage increases by 1d4 when you reach 5th level (2d4), 11th level
(3d4), and 17th level (4d4).
    """.strip()
    character_class = [classes.Bard]
    level = 0
    cast_range = 60
    school = 'Enchantment'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'V'
    concentration = False


class Alarm(Spell):
    name = 'Alarm (Ritual)'
    description = """
You set an alarm against unwanted intrusion.
Choose a door, a window, or an area within range that is no larger than a
20-foot cube. Until the spell ends, an alarm alerts you whenever a tiny or
larger creature touches or enters the warded area. When you cast the spell,
you can designate creatures that won’t set off the alarm. You also choose
whether the alarm is mental or audible.

A mental alarm alerts you with a ping in your mind if you are within 1 mile of
the warded area. This ping awakens you if you are sleeping.
An audible alarm produces the sound of a hand bell for 10 seconds within 60
feet.
    """.strip()
    character_class = [classes.Ranger, classes.Wizard]
    level = 1
    cast_range = 30
    school = 'Abjuration'
    ritual = True
    casting_time = '1 minute'
    duration = 8 * 60 * 60
    components = 'VSM (a tiny bell and a piece of fine silver wire)'
    concentration = False


class AnimalFriendship(Spell):
    name = 'Animal Friendship'
    description = """
This spell lets you convince a beast that you mean it no harm.
Choose a beast that you can see within range. It must see and hear you. If the
beast’s Intelligence is 4 or higher, the spell fails. Otherwise, the beast must
succeed on a Wisdom saving throw or be charmed by you for the spell’s duration.
If you or one of your companions harms the target, the spell ends.

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, you can
affect one additional beast for each slot level above 1st.
    """.strip()
    character_class = [classes.Bard, classes.Druid, classes.Ranger]
    level = 1
    cast_range = 30
    school = 'Enchantment'
    ritual = False
    casting_time = '1 action'
    duration = 24 * 60 * 60
    components = 'VSM (a morsel of food)'
    concentration = False


class ArmorOfAgathys(Spell):
    name = 'Armor of Agathys'
    description = """
A protective magical force surrounds you, manifesting as a spectral frost that
covers you and your gear.
You gain 5 temporary hit points for the duration. If a creature hits you with a
melee attack while you have these hit points, the creature takes 5 cold damage. 

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, both the
temporary hit points and the cold damage increase by 5 for each slot.
    """.strip()
    character_class = [classes.Warlock]
    level = 1
    cast_range = -1
    school = 'Abjuration'
    ritual = False
    casting_time = '1 action'
    duration = 60 * 60
    components = 'VSM (a cup of water)'
    concentration = False


class ArmsOfHadar(Spell):
    name = 'Arms of Hadar'
    description = """
You invoke the power of Hadar, the Dark Hunger.
Tendrils of dark energy erupt from you and batter all creatures within 10 feet
of you. Each creature in that area must make a Strength saving throw. On a
failed save, a target takes 2d6 necrotic damage and can’t take reactions until
its next turn. On a successful save, the creature takes half damage, but
suffers no other effect. 

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, the damage
increases by 1d6 for each slot level above 1st.
    """.strip()
    character_class = [classes.Warlock]
    level = 1
    cast_range = -1
    school = 'Conjuration'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class Bane(Spell):
    name = 'Bane'
    description = """
Up to three creatures of your choice that you can see within range must make
Charisma saving throws. Whenever a target that fails this saving throw makes an
attack roll or a saving throw before the spell ends, the target must roll a d4
and subtract the number rolled from the attack roll or saving throw.

~~ At higher level ~~
When you cast this spell using a spelslot of 2nd level or higher, you can
target one aditional creature for each slot level above 1st.
    """.strip()
    character_class = [classes.Bard, classes.Cleric]
    level = 1
    cast_range = 30
    school = 'Enchantment'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'VSM (a drop of blood)'
    concentration = True


class Bless(Spell):
    name = 'Bless'
    description = """
You bless up to three creatures of your choice within range. Whenever a target
makes an attack roll or a saving throw before the spell ends, the target can
roll a d4 and add the number rolled to the attack roll or saving throw. 

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, you can
target one additional creature for each slot level above 1st.
    """.strip()
    character_class = [classes.Cleric, classes.Paladin]
    level = 1
    cast_range = 30
    school = 'Enchantment'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'VSM (a sprinkling of holy water)'
    concentration = True


class BurningHands(Spell):
    name = 'Burning Hands'
    description = """
As you hold your hands with thumbs touching and fingers spread, a thin sheet of
flames shoots forth from your outstretched fingertips. Each creature in a
15-foot cone must make a Dexterity saving throw. A creature takes 3d6 fire
damage on a failed save, or half as much damage on a successful one.

The fire ignites any flammable objects in the area that aren’t being worn or
carried. 

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, the damage
increases by 1d6 for each slot level above 1st.
    """.strip()
    character_class = [classes.Sorcerer, classes.Wizard]
    level = 1
    cast_range = -1
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class CharmPerson(Spell):
    name = 'Charm Person'
    description = """
You attempt to charm a humanoid you can see within range.
It must make a Wisdom saving throw, and does so with advantage if you or your
companions are fighting it. If it fails the saving throw, it is charmed by you
until the spell ends or until you or your companions do anything harmful to it.
The charmed creature regards you as a friendly acquaintance. When the spell
ends, the creature knows it was charmed by you.

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, you can
target one additional creature for each slot level above 1st. The creatures
must be within 30 feet of each other when you target them.
    """.strip()
    character_class = [
        classes.Bard, classes.Druid, classes.Sorcerer,
        classes.Warlock, classes.Wizard
    ]
    level = 1
    cast_range = 30
    school = 'Enchantment'
    ritual = False
    casting_time = '1 action'
    duration = 60 * 60
    components = 'VS'
    concentration = False


class ChromaticOrb(Spell):
    name = 'Chromatic Orb'
    description = """
You hurl a 4-inch-diameter sphere of energy at a creature that you can see
within range. You choose acid, cold, fire, lightning, poison, or thunder for
the type of orb you create, and then make a ranged spell attack against the
target. If the attack hits, the creature takes 3d8 damage of the type you
chose. 

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, the damage
increases by 1d8 for each slot level above 1st.
    """.strip()
    character_class = [classes.Sorcerer, classes.Wizard]
    level = 1
    cast_range = 90
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VSM (a diamond worth at least 50gp)'
    concentration = False


class ColorSpray(Spell):
    name = 'Color Spray'
    description = """
A dazzling array of flashing, colored light springs from your hand.
Roll 6d10, the total is how many hit points of creatures this spell can effect.
Creatures in a 15-foot cone originating from you are affected in ascending
order of their current hit points (ignoring unconscious creatures and creatures
that can’t see).

Starting with the creature that has the lowest current hit points, each
creature affected by this spell is blinded until the spell ends. Subtract each
creature’s hit points from the total before moving on to the creature with the
next lowest hit points. A creature’s hit points must be equal to or less than
the remaining total for the creature to be affected. 

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, roll an
additional 2d10 for each slot level above 1st.
    """.strip()
    character_class = [classes.Sorcerer, classes.Wizard]
    level = 1
    cast_range = -1
    school = 'Illusion'
    ritual = False
    casting_time = '1 action'
    duration = 6
    components = 'VSM'
    concentration = False


class Command(Spell):
    name = 'Command'
    description = """
You speak a one-word command to a creature you can see within range.
The target must succeed on a Wisdom saving throw or follow the command on its
next turn. The spell has no effect if the target is undead, if it doesn’t
understand your language, or if your command is directly harmful to it. Some
typical commands and their effects follow. You might issue a command other than
one described here. If you do so, the DM determines how the target behaves. If
the target can’t follow your command, the spell ends.
• Approach - The target moves toward you by the shortest and most direct route,
    ending its turn if it moves within 5 feet of you.
• Drop - The target drops whatever it is holding and then ends its turn.
• Flee - The target spends its turn moving away from you by the fastest
    available means.
• Grovel - The target falls prone and then ends its turn.
• Halt - The target doesn’t move and takes no actions. A flying creature stays
    aloft, provided that it is able to do so. If it must move to stay aloft, it
    flies the minimum distance needed to remain in the air. 

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, you can
affect one additional creature for each slot level above 1st. The creatures
must be within 30 feet of each other when you target them
    """.strip()
    character_class = [classes.Cleric, classes.Paladin]
    level = 1
    cast_range = 60
    school = 'Enchantment'
    ritual = False
    casting_time = '1 action'
    duration = 6
    components = 'V'
    concentration = False


class CompelledDuel(Spell):
    name = 'Compelled Duel'
    description = """
You attempt to compel a creature into a duel.
One creature that you can see within range must make a Wisdom saving throw. On
a failed save, the creature is drawn to you, compelled by your divine demand.
For the duration, it has disadvantage on attack rolls against creatures other
than you, and must make a Wisdom saving throw each time it attempts to move to
a space that is more than 30 feet away from you; if it succeeds on this saving
throw, this spell doesn’t restrict the target’s movement for that turn.

The spell ends if you attack any other creature, if you cast a spell that
targets a hostile creature other than the target, if a creature friendly to you
damages the target or casts a harmful spell on it, or if you end your turn more
than 30 feet away from the target.
    """.strip()
    character_class = [classes.Paladin]
    level = 1
    cast_range = 30
    school = 'Enchantment'
    ritual = False
    casting_time = '1 bonus action'
    duration = 60
    components = 'V'
    concentration = True


class ComprehendLanguages(Spell):
    name = 'Comprehend Languages (Ritual)'
    description = """
For the duration, you understand the literal meaning of any spoken language
that you hear.
You also understand any spoken language that you hear. You also understand any
written language that you see, but you must be touching the surface of which
the words are written. It takes about 1 minute to read one page of text.

This spell doesn’t decode secret messages in a text or glyph, such as an arcane
sigil, that isn’t part of a written language.
    """.strip()
    character_class = [
        classes.Bard, classes.Sorcerer, classes.Warlock, classes.Wizard
    ]
    level = 1
    cast_range = -1
    school = 'Divination'
    ritual = True
    casting_time = '1 action'
    duration = 60 * 60
    components = 'VSM (a pinch of soot and salt)'
    concentration = False


class CreateOrDestroyWater(Spell):
    name = 'Create or Destroy Water'
    description = """
You either create or destroy water.

Create Water
You create up to 10 gallons of clean water within range in an open container.
Alternatively, the water falls as rain in a 30-foot cube within range,
extinguishing exposed flames in the area.

Destroy Water 
You destroy up to 10 gallons of water in an open container within range.
Alternatively, you destroy fog in a 30-foot cube within range. 

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, you create
or destroy 10 additional gallons of water, or the size of the cube increases by
5 feet, for each slot level above 1st.
    """.strip()
    character_class = [classes.Cleric, classes.Druid]
    level = 1
    cast_range = 30
    school = 'Transmutation'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VSM (a drop of water if creating water or a few grains of '+\
        'sand if destroying it)'
    concentration = False


class CureWounds(Spell):
    name = 'Cure Wounds'
    description = """
A creature you touch regains a number of hit points equal to 1d8 + your
spellcasting ability modifier. This spell has no effect on undead or
constructs. 

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, the healing
increases by 1d8 for each slot level above 1st.
    """.strip()
    character_class = [
        classes.Bard, classes.Cleric, classes.Druid,
        classes.Paladin, classes.Ranger
    ]
    level = 1
    cast_range = 0
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class DetectEvilAndGood(Spell):
    name = 'Detect Evil and Good'
    description = """
For the duration, you know if there is an aberration, celestial, elemental,
fey, fiend, or undead within 30 feet of you, as well as where the creature is
located. Similarly, you know if there is a place or object within 30 feet of
you that has been magically consecrated or desecrated.

The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1
inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt.
    """.strip()
    character_class = [classes.Cleric, classes.Paladin]
    level = 1
    cast_range = -1
    school = 'Divination'
    ritual = False
    casting_time = '1 action'
    duration = 10 * 60
    components = 'VS'
    concentration = True


class DetectMagic(Spell):
    name = 'Detect Magic (Ritual)'
    description = """
For the duration, you sense the presence of magic within 30 feet of you. If you
sense magic in this way, you can use your action to see a faint aura around any
visible creature or object in the area that bears magic, and you learn its
school of magic, if any.

The spell can penetrate most barriers, but is blocked by 1 foot of stone, 1
inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt.
    """.strip()
    character_class = [
        classes.Bard, classes.Cleric, classes.Paladin,
        classes.Ranger, classes.Sorcerer, classes.Wizard
    ]
    level = 1
    cast_range = -1
    school = 'Divination'
    ritual = True
    casting_time = '1 action'
    duration = 10 * 60
    components = 'VS'
    concentration = True


class DetectPoisonAndDisease(Spell):
    name = 'Detect Poison and Disease (Ritual)'
    description = """
For the duration, you can sense the presence and location of poisons, poisonous
creatures, and diseases within 30 feet of you. You also identify the kind of
poison, poisonous creature, or disease in each case.

The spell can penetrate most barriers, but is blocked by 1 foot of stone, 1
inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt.
    """.strip()
    character_class = [
        classes.Cleric, classes.Druid, classes.Paladin, classes.Ranger
    ]
    level = 1
    cast_range = -1
    school = 'Divination'
    ritual = True
    casting_time = '1 action'
    duration = 10 * 60
    components = 'VSM (a yew leaf)'
    concentration = True


class DisguiseSelf(Spell):
    name = 'Disguise Self'
    description = """
You make yourself – including your clothing, armor, weapons, and other
belongings on your person – look different until the spell ends or until you
use your action to dismiss it.
You can seem 1 foot shorter or taller and can appear thin, fat, or in between.
You can’t change your body type, so you must adopt a form that has the same
basic arrangement of limbs. Otherwise, the extent of the illusion is up to you.

The changes wrought by this spell fail to hold up to physical inspection. For
example, if you use this spell to add a hat to your outfit, objects pass
through the hat, and anyone who touches it would feel nothing or would feel
your head and hair. If you use this spell to appear thinner than you are, the
hand of som eone who reaches out to touch you would bump into you while it was
seemingly still in midair. To discern that you are disguised, a creature can
use its action to inspect your appearance and must succeed on an Intelligence
(Investigation) check against your spell save DC.
    """.strip()
    character_class = [classes.Bard, classes.Sorcerer, classes.Wizard]
    level = 1
    cast_range = -1
    school = 'Illusion'
    ritual = False
    casting_time = '1 action'
    duration = 60 * 60
    components = 'VS'
    concentration = False


class DissonantWhispers(Spell):
    name = 'Dissonant Whispers'
    description = """
You whisper a discordant melody that only one creature of your choice within
range can hear, wracking it with terrible pain.
The target must make a Wisdom saving throw. On a failed save, it takes 3d6
psychic damage and must immediately use its reaction , if available, to move as
far as its speed allows away from you. The creature doesn’t move into obviously
dangerous ground, such as a fire or a pit. On a successful save, the target
takes half as much damage and doesn’t have to move away. A deafened creature
automatically succeeds on the save. 

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, the damage
increases by 1d6 for each slot level above 1st
    """.strip()
    character_class = [classes.Bard]
    level = 1
    cast_range = 60
    school = 'Enchantment'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'V'
    concentration = False


class DivineFavor(Spell):
    name = 'Divine Favor'
    description = """
Your prayer empowers you with divine radiance. Until the spell ends, your
weapon attacks deal and extra 1d4 radiant damage on a hit.
    """.strip()
    character_class = [classes.Paladin]
    level = 1
    cast_range = -1
    school = 'Evocation'
    ritual = False
    casting_time = '1 bonus action'
    duration = 60
    components = 'VS'
    concentration = True


class EnsnaringStrike(Spell):
    name = 'Ensnaring Strike'
    description = """
The next time you hit a creature with a weapon attack before this spell ends, a
writhing mass of thorny vines appears at the point of impact, and the target
must succeed on a Strength saving throw or be restrained by the magical vines
until the spell ends. A Large or larger creature has advantage on this saving
throw. If the target succeeds on the save, the vines shrivel away.

While restrained by this spell, the target takes 1d6 piercing damage at the
start of each of its turns. A creature restrained by the vines or one that can
touch the creature can use its action to make a Strength check against your
spell save DC. On a success, the target is freed. 

~~ At higher level ~~
If you cast this spell using a spell slot of 2nd level or higher, the damage
increases by 1d6 for each slot level above 1st.
    """.strip()
    character_class = [classes.Ranger]
    level = 1
    cast_range = -1
    school = 'Conjuration'
    ritual = False
    casting_time = '1 bonus action'
    duration = 60
    components = 'V'
    concentration = True


class Entangle(Spell):
    name = 'Entangle'
    description = """
Grasping weeds and vines sprout from the ground in a 20-foot square starting
from a point within range. For the duration, these plants turn the ground in
the area into difficult terrain.

A creature in the area when you cast the spell must succeed on a Strength
saving throw or be restrained by the entangling plants until the spell ends. A
creature restrained by the plants can use its action to make a Strength check
against your spell save DC. On a success, it frees itself.

When the spell ends, the conjured plants wilt away.
    """.strip()
    character_class = [classes.Druid]
    level = 1
    cast_range = 90
    school = 'Conjuration'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'VS'
    concentration = True


class ExpeditiousRetreat(Spell):
    name = 'Expeditious Retreat'
    description = """
This spell allows you to move at an incredible pace. When you cast this spell,
and then as a bonus action on each of your turns until the spell ends, you can
take the Dash action.
    """.strip()
    character_class = [classes.Sorcerer, classes.Warlock, classes.Wizard]
    level = 1
    cast_range = -1
    school = 'Transmutation'
    ritual = False
    casting_time = '1 bonus action'
    duration = 10 *60
    components = 'VS'
    concentration = True


class FaerieFire(Spell):
    name = 'Faerie Fire'
    description = """
Each object in a 20-foot cube within range is outlined in blue, green, or
violet light (your choice).
Any creature in the area when the spell is cast is also outlined in light if it
fails a Dexterity saving throw. For the duration, objects and affected
creatures shed dim light in a 10-foot radius.

Any attack roll against an affected creature or object has advantage if the
attacker can see it, and the affected creature or object can’t benefit from
being invisible.
    """.strip()
    character_class = [classes.Bard, classes.Druid]
    level = 1
    cast_range = 60
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'V'
    concentration = True


class FalseLife(Spell):
    name = 'False Life'
    description = """
Bolstering yourself with a necromantic facsimile of life, you gain 1d4 + 4
temporary hit points for the duration. 

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, you gain 5
additional temporary hit points for each slot level above 1st.
    """.strip()
    character_class = [classes.Sorcerer, classes.Wizard]
    level = 1
    cast_range = -1
    school = 'Necromancy'
    ritual = False
    casting_time = '1 action'
    duration = 60 * 60
    components = 'VSM (a small amount of alcohol or distilled spirits)'
    concentration = False


class FeatherFall(Spell):
    name = 'Feather Fall'
    description = """
Reaction: When you or a creature within 60 feet of you falls.

Choose up to five falling creatures within range. A falling creature’s rate of
descent slows to 60 feet per round until the spell ends. If the creature lands
before the spell ends, it takes no falling damage and can land on its feet, and
the spell ends for that creature.
    """.strip()
    character_class = [classes.Bard, classes.Sorcerer, classes.Wizard]
    level = 1
    cast_range = 60
    school = 'Transmutation'
    ritual = False
    casting_time = '1 reaction'
    duration = 60
    components = 'VM (a small feather or piece of down)'
    concentration = False


class FindFamiliar(Spell):
    name = 'Find Familiar (Ritual)'
    description = """
You gain the service of a familiar, a spirit that takes an animal form you
choose: bat, cat, crab, frog (toad), hawk. lizard, octopus, owl, poisonous
snake, fish (quipper), rat, raven, sea horse, spider, or weasel. Appearing in
an unoccupied space within range, the familiar has the statistics of the chosen
form, though it is a celestial, fey or fiend (your choice) instead of a beast.

Your familiar acts independently of you, but it always obeys your commands. In
combat, it rolls its own initiative and acts on its own turn. A familiar can’t
attack, but it can take other actions as normal.

When the familiar drops to 0 hit points, it disappears, leaving behind no
physical form. It reappears after you cast this spell again.

While your familiar is within 100 feet of you, you can communicate with it
telepathically. Additionally, as an action, you can see through your familiar’s
eyes and hear what it hears until the start of your next turn, gaining the
benefits of any special senses that the familiar has. During this time, you are
deaf and blind with regard to your own senses.

As an action, you can temporarily dismiss your familiar. It disappears into a
pocket dimension where it awaits you summons. Alternatively, you can dismiss it
forever. As an action while it is temporarily dismissed, you can cause it to
reappear in any unoccupied space within 30 feet of you.

You can’t have more than one familiar at a time. If you cast this spell while
you already have a familiar, you instead cause it to adopt a new form. Choose
one of the forms from the above list. Your familiar transforms into the chosen
creature.

Finally, when you cast a spell with a range of touch, your familiar can deliver
the spell as if it had cast the spell. Your familiar must be within 100 feet of
you, and it must use its reaction to deliver the spell when you cast it. If the
spell requires an attack roll, you use your attack modifier for the roll.
    """.strip()
    character_class = [classes.Wizard]
    level = 1
    cast_range = 10
    school = 'Conjuration'
    ritual = True
    casting_time = '1 hour'
    duration = 0
    components = 'VSM (10 gp worth of charcoal, incense, and herbs that ' +\
        'must be consumed by fire in a brass brazier)'
    concentration = False


class FogCloud(Spell):
    name = 'Fog Cloud'
    description = """
You create a 20-foot-radius sphere of fog centered on a point within range. The
sphere spreads around corners, and its area is heavily obscured, It lasts for
the duration or until a wind of moderate or greater speed (at least 10 miles
per hour) disperses it.

At higher level
When you cast this spell using a spell slot of 2nd level or higher, the radius
of the fog increases by 20 feet for each slot level above 1st.
    """.strip()
    character_class = [
        classes.Druid, classes.Ranger, classes.Sorcerer, classes.Wizard
    ]
    level = 1
    cast_range = 120
    school = 'Conjuration'
    ritual = False
    casting_time = '1 action'
    duration = 60 * 60
    components = 'VS'
    concentration = True


class Goodberry(Spell):
    name = 'Goodberry'
    description = """
Up to ten berries appear in your hand and are infused with magic for the
duration. A creature can use its action to eat one berry. Eating a berry
restores 1 hit point, and the berry provides enough nourishment to sustain a
creature for one day.
The berries lose their potency if they have not been consumed within 24 hours
of the casting of this spell.
    """.strip()
    character_class = [classes.Druid, classes.Ranger]
    level = 1
    cast_range = 0
    school = 'Transmutation'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VSM (a sprig of mistletoe)'
    concentration = False


class Grease(Spell):
    name = 'Grease'
    description = """
Slick grease covers the ground in a 10-foot square centered on a point within
range and turns it into difficult terrain for the duration.

When the grease appears, each creature standing in its area must succeed on a
Dexterity saving throw or fall prone. A creature that enters the area or ends
its turn there must also succeed on a Dexterity saving throw or fall prone.
    """.strip()
    character_class = [classes.Wizard]
    level = 1
    cast_range = 60
    school = 'Conjuration'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'VSM (a bit of pork rind or butter)'
    concentration = False


class GuidingBolt(Spell):
    name = 'Guiding Bolt'
    description = """
A flash of light streaks toward a creature of your choice within range.
Make a ranged spell attack against the target. On a hit, the target takes 4d6
radiant damage, and the next attack roll made against this target before the
end of your next turn has advantage, thanks to the mystical dim light
glittering on the target until then. 

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, the damage
increases by 1d6 for each slot level above 1st.
    """.strip()
    character_class = [classes.Cleric]
    level = 1
    cast_range = 120
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 6
    components = 'VS'
    concentration = False


class HailOfThorns(Spell):
    name = 'Hail of Thorns'
    description = """
The next time you hit a creature with a ranged weapon attack before the spell
ends, this spell creates a rain of thorns that sprouts from your ranged weapon
or ammunition. In addition to the normal effect of the attack, the target of
the attack and each creature within 5 feet of it must make a Dexterity saving
throw. A creature takes 1d10 piercing damage on a failed save, or half as much
damage on a successful one.

~~ At higher level ~~
If you cast this spell using a spell slot of 2nd level or higher, the damage
increases by 1d10 for each slot level above 1st (to a maximum of 6d10).
    """.strip()
    character_class = [classes.Ranger]
    level = 1
    cast_range = -1
    school = 'Conjuration'
    ritual = False
    casting_time = '1 bonus action'
    duration = 60
    components = 'V'
    concentration = True


class HealingWord(Spell):
    name = 'Healing Word'
    description = """
A creature of your choice that you can see within range regains hit points
equal to 1d4 + your spellcasting ability modifier.
This spell has no effect on undead or constructs.

At higher level
When you cast this spell using a spell slot of 2nd level or higher, the healing
increases by 1d4 for each slot level above 1st.
    """.strip()
    character_class = [classes.Bard, classes.Cleric, classes.Druid]
    level = 1
    cast_range = 60
    school = 'Evocation'
    ritual = False
    casting_time = '1 bonus action'
    duration = 0
    components = 'V'
    concentration = False


class HellishRebuke(Spell):
    name = 'Hellish Rebuke'
    description = """
Reaction: you are being damaged by a creature within 60 feet of you that you
can see.

You point your finger, and the creature that damaged you is momentarily
surrounded by hellish flames. The creature must make a Dexterity saving throw.
It takes 2d10 fire damage on a failed save, or half as much damage on a
successful one.

At higher level
When you cast this spell using a spell slot of 2nd level or higher, the damage
increases by 1d10 for each slot level above 1st.
    """.strip()
    character_class = [classes.Warlock]
    level = 1
    cast_range = 60
    school = 'Evocation'
    ritual = False
    casting_time = '1 reaction'
    duration = 0
    components = 'VS'
    concentration = False


class Heroism(Spell):
    name = 'Heroism'
    description = """
A willing creature you touch is imbued with bravery.
Until the spell ends, the creature is immune to being frightened and gains
temporary hit points equal to your spellcasting ability modifier at the start
of each of its turns. When the spell ends, the target loses any remaining
temporary hit points from this spell.

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, you can
target one additional creature for each slot level above 1st.
    """.strip()
    character_class = [classes.Bard, classes.Paladin]
    level = 1
    cast_range = 0
    school = 'Enchantment'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'VS'
    concentration = True


class Hex(Spell):
    name = 'Hex'
    description = """
You place a curse on a creature that you can see within range. Until the spell
ends, you deal an extra 1d6 necrotic damage to the target whenever you hit it
with an attack. Also, choose one ability when you cast the spell. The target
has disadvantage on ability checks made with the chosen ability.

If the target drops to 0 hit points before this spell ends, you can use a bonus
action on a subsequent turn of yours to curse a new creature.

A remove curse cast on the target ends this spell early.

~~ At higher level ~~
When you cast this spell using a spell slot of 3rd or 4th level, you can
maintain your concentration on the spell for up to 8 hours.
When you use a spell slot of 5th level or higher, you can maintain your
concentration on the spell for up to 24 hours.
    """.strip()
    character_class = [classes.Warlock]
    level = 1
    cast_range = 90
    school = 'Enchantment'
    ritual = False
    casting_time = '1 bonus action'
    duration = 60 * 60
    components = 'VSM (the petrified eye of a newt)'
    concentration = True


class HuntersMark(Spell):
    name = 'Hunter\'s Mark'
    description = """
You choose a creature you can see within range and mystically mark it as your
quarry.
Until the spell ends, you deal an extra 1d6 damage to the target whenever you
hit it with a weapon attack, and you have advantage on any Wisdom (Perception)
or Wisdom (Survival) check you make to find it. If the target drops to 0 hit
points before this spell ends, you can use a bonus action on a subsequent turn
of yours to mark a new creature.

~~ At higher level ~~
When you cast this spell using a spell slot of 3rd or 4th level, you can
maintain your concentration on the spell for up to 8 hours.
When you use a spell slot of 5th level or higher, you can maintain your
concentration on the spell for up to 24 hours.
    """.strip()
    character_class = [classes.Ranger]
    level = 1
    cast_range = 90
    school = 'Divination'
    ritual = False
    casting_time = '1 bonus action'
    duration = 90
    components = 'V'
    concentration = True


class Identify(Spell):
    name = 'Identify (Ritual)'
    description = """
You choose one object that you must touch throughout the casting of the spell.
If it is a magic item or some other magic-imbued object, you learn its
properties and how to use them, whether it requires attunement to use, and how
many charges it has, if any. You learn whether any spells are affecting the
item and what they are. If the item was created by a spell, you learn which
spell created it.

If you instead touch a creature throughout the casting, you learn what spells,
if any, are currently affecting it.
    """.strip()
    character_class = [classes.Bard, classes.Wizard]
    level = 1
    cast_range = 0
    school = 'Divination'
    ritual = True
    casting_time = '1 minute'
    duration = 0
    components = 'VSM (a pearl worth at least 100 gp and an owl feather)'
    concentration = False


class IllusoryScript(Spell):
    name = 'Illusory Script (Ritual)'
    description = """
You write on parchment, paper, or some other suitable writing material and
imbue it with a potent illusion that lasts for the duration.

To you and any creatures you designate when you cast the spell, the writing
appears normal, written in your hand, and conveys whatever meaning you intended
when you wrote the text. To all others, the writing appears as if it were
written in an unknown or magical script that is unintelligible. Alternatively,
you can cause the writing to appear to be an entirely different message,
written in a different hand and language, though the language must be one you
know.

Should the spell be dispelled, the original script and the illusion both
disappear.
A creature with truesight can read the hidden message.
    """.strip()
    character_class = [classes.Bard, classes.Warlock, classes.Wizard]
    level = 1
    cast_range = 0
    school = 'Illusion'
    ritual = True
    casting_time = '1 minute'
    duration = 10 * 24 * 60 * 60
    components = 'SM (a lead-based ink worth at least 10 gp, which the ' + \
        'spell consumes)'
    concentration = False


class InflictWounds(Spell):
    name = 'Inflict Wounds'
    description = """
Make a melee spell attack against a creature you can reach. On a hit, the
target takes 3d10 necrotic damage.

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, the damage
increases by 1d10 for each slot level above 1st.
    """.strip()
    character_class = [classes.Cleric]
    level = 1
    cast_range = 0
    school = 'Necromancy'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class Jump(Spell):
    name = 'Jump'
    description = """
You touch a creature. The creature’s jump distance is tripled until the spell
ends.
    """.strip()
    character_class = [
        classes.Druid, classes.Ranger, classes.Sorcerer, classes.Wizard
    ]
    level = 1
    cast_range = 0
    school = 'Transmutation'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'VSM (a grasshopper\'s hind leg)'
    concentration = False


class Longstrider(Spell):
    name = 'Longstrider'
    description = """
You touch a creature. The target’s speed increases by 10 feet until the spell
ends.

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, you can
target one additional creature for each slot level above 1st.
    """.strip()
    character_class = [
        classes.Bard, classes.Druid, classes.Ranger, classes.Wizard
    ]
    level = 1
    cast_range = 0
    school = 'Transmutation'
    ritual = False
    casting_time = '1 action'
    duration = 60 * 60
    components = 'VSM (a pinch of dirt)'
    concentration = False


class MageArmor(Spell):
    name = 'Mage Armor'
    description = """
You touch a willing creature who isn’t wearing armor, and a protective magical
force surrounds it until the spell ends. The target’s base AC becomes 13 + its
Dexterity modifier. The spell ends it if the target dons armor or if you
dismiss the spell as an action.
    """.strip()
    character_class = [classes.Sorcerer, classes.Wizard]
    level = 1
    cast_range = 0
    school = 'Abjuration'
    ritual = False
    casting_time = '1 action'
    duration = 8 * 60 * 60
    components = 'VSM (a piece of cured leather)'
    concentration = False


class MagicMissile(Spell):
    name = 'Magic Missile'
    description = """
You create three glowing darts of magical force. Each dart hits a creature of
your choice that you can see within range. A dart deals 1d4 + 1 force damage to
its target. The darts all strike simultaneously and you can direct them to hit
one creature or several.

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, the spell
creates one more dart for each slot level above 1st.
    """.strip()
    character_class = [classes.Sorcerer, classes.Wizard]
    level = 1
    cast_range = 120
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class ProtectionFromEvilAndGood(Spell):
    name = 'Protection from Evil and Good'
    description = """
Until the spell ends, one willing creature you touch is protected against
certain types of creatures: aberrations, celestials, elementals, fey, fiends,
and undead.

The protection grants several benefits. Creatures of those types have
disadvantage on attack rolls against the target. The target also can’t be
charmed, frightened, or possessed by them. If the target is already charmed,
frightened, or possessed by such a creature, the target has advantage on any
new saving throw against the relevant effect.
    """.strip()
    character_class = [
        classes.Cleric, classes.Paladin, classes.Warlock, classes.Wizard
    ]
    level = 1
    cast_range = 0
    school = 'Abjuration'
    ritual = False
    casting_time = '1 action'
    duration = 10 * 60
    components = 'VSM (holy water or powdered silver and iron, which the ' + \
        'spell consumes)'
    concentration = True


class PurifyFoodAndDrink(Spell):
    name = 'Purify Food and Drink (Ritual)'
    description = """
All nonmagical food and drink within a 5-foot-radius sphere centered on a point
of your choice within range is purified and rendered free of poison and
disease.
    """.strip()
    character_class = [classes.Cleric, classes.Druid, classes.Paladin]
    level = 1
    cast_range = 10
    school = 'Transmutation'
    ritual = True
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class RayOfSickness(Spell):
    name = 'Ray of Sickness'
    description = """
A ray of sickening greenish energy lashes out toward a creature within range.
Make a ranged spell attack against the target. On a hit, the target takes 2d8
poison damage and must make a Constitution saving throw. On a failed save, it
is also poisoned until the end of your next turn.

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, the damage
increases by 1d8 for each slot level above 1st.
    """.strip()
    character_class = [classes.Sorcerer, classes.Wizard]
    level = 1
    cast_range = 60
    school = 'Necromancy'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class Sanctuary(Spell):
    name = 'Sanctuary'
    description = """
You ward a creature within range against attack.
Until the spell ends, any creature who targets the warded creature with an
attack or a harmful spell must first make a Wisdom saving throw. On a failed
save, the creature must choose a new target or lose the attack or spell. This
spell doesn’t protect the warded creature from area effects, such as the
explosion of a fireball.

If the warded creature makes an attack or casts a spell that affects an enemy
creature, this spell ends.
    """.strip()
    character_class = [classes.Cleric]
    level = 1
    cast_range = 30
    school = 'Abjuration'
    ritual = False
    casting_time = '1 bonus action'
    duration = 60
    components = 'VSM (a small silver mirror)'
    concentration = False


class SearingSmite(Spell):
    name = 'Searing Smite'
    description = """
The next time you hit a creature with a melee weapon attack during the spell’s
duration, your weapon flares with white-hot intensitity, and the attack deals
an extra 1d6 fire damage to the target and causes the target to ignite in
flames.

At the start of each of its turns until the spell ends, the target must make a
Constitution saving throw. On a failed save, it takes 1d6 fire damage. On a
successful save, the spells ends. If the target or a creature within 5 feet of
it uses an action to put out the flames, or if some other effect douses the
flames (such as the target being submerged in water), the spell ends.

At higher level
When you cast this spell using a spell slot of 2nd level or higher, the initial
extra damage dealt by the attack increases by 1d6 for each slot
    """.strip()
    character_class = [classes.Paladin]
    level = 1
    cast_range = -1
    school = 'Evocation'
    ritual = False
    casting_time = '1 bonus action'
    duration = 60
    components = 'V'
    concentration = True


class Shield(Spell):
    name = 'Shield'
    description = """
Reaction trigger: You are hit by an attack or targeted by the magic missile
spell

An invisible barrier of magical force appears and protects you. Until the start
of your next turn, you have a +5 bonus to AC, including against the triggering
attack, and you take no damage from magic missile.
    """.strip()
    character_class = [classes.Sorcerer, classes.Wizard]
    level = 1
    cast_range = -1
    school = 'Abjuration'
    ritual = False
    casting_time = '1 reaction'
    duration = 6
    components = 'VS'
    concentration = False


class ShieldOfFaith(Spell):
    name = 'Shield of Faith'
    description = """
A shimmering field appears and surrounds a creature of your choice within
range, granting it a +2 bonus to AC for the duration.
    """.strip()
    character_class = [classes.Cleric, classes.Paladin]
    level = 1
    cast_range = 60
    school = 'Abjuration'
    ritual = False
    casting_time = '1 bonus action'
    duration = 10 * 60
    components = 'VSM (a small parchment with a bit of holy text)'
    concentration = True


class SilentImage(Spell):
    name = 'Silent Image'
    description = """
You create the image of an object, a creature, or some other visible phenomenon
that is no larger than a 15-foot cube. The image appears at a spot within range
and lasts for the duration. The image is purely visual; it isn’t accompanied by
sound, smell, or other sensory effects.

You can use your action to cause the image to move to any spot within range. As
the image changes location, you can alter its appearance so that its movements
appear natural for the image. For example, if you create an image of a creature
and move it, you can alter the image so that it appears to be walking.

Physical interaction with the image reveals it to be an illusion, because
things can pass through it. A creature that uses its action to examine the
image can determine that it is an illusion with a successful Intelligence
(Investigation) check against your spell save DC. If a creature discerns the
illusion for what it is, the creature can see through the image.
    """.strip()
    character_class = [classes.Bard, classes.Sorcerer, classes.Wizard]
    level = 1
    cast_range = 60
    school = 'Illusion'
    ritual = False
    casting_time = '1 action'
    duration = 10 * 60
    components = 'VSM (a bit of fleece)'
    concentration = True


class Sleep(Spell):
    name = 'Sleep'
    description = """
This spell sends creatures into a magical slumber. Roll 5d8, the total is how
many hit points of creatures this spell can affect. Creatures within 20 feet of
a point you choose within range are affected in ascending order of their
current hit points (ignoring unconscious creatures).

Starting with the creature that has the lowest current hit points, each
creature affected by this spell falls unconscious until the spell ends, the
sleeper takes damage, or someone uses an action to shake or slap the sleeper
awake. Subtract each creature’s hit points from the total before moving on to
the creature with the next lowest hit points. A creature’s hit points must be
equal to or less than the remaining total for that creature to be affected.
Undead and creatures immune to being charmed aren’t affected by this spell.

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, roll an
additional 2d8 for each slot level above 1st.
    """.strip()
    character_class = [classes.Bard, classes.Sorcerer, classes.Wizard]
    level = 1
    cast_range = 90
    school = 'Enchantment'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'VSM (a pinch of fine sane, rose petals, or a cricket)'
    concentration = False


class SpeakWithAnimals(Spell):
    name = 'Speak with Animals (Ritual)'
    description = """
You gain the ability to comprehend and verbally communicate with beasts for the
duration.
The knowledge and awareness of many beasts is limited by their intelligence,
but at minimum, beasts can give you information about nearby locations and
monsters, including whatever they can perceive or have perceived within the
past day. You might be able to persuade a beast to perform a small favor for
you, at the DM’s discretion.
    """.strip()
    character_class = [classes.Bard, classes.Druid, classes.Ranger]
    level = 1
    cast_range = -1
    school = 'Divination'
    ritual = True
    casting_time = '1 action'
    duration = 10 * 60
    components = 'VS'
    concentration = False


class TashasHideousLaughter(Spell):
    name = 'Tasha\'s Hideous Laughter'
    description = """
A creature of your choice that you can see within range perceives everything as
hilariously funny and falls into fits of laughter if this spell affects it. The
target must succeed on a Wisdom saving throw or fall prone, becoming
incapacitated and unable to stand up for the duration. A creature with an
Intelligence score of 4 or less isn’t affected.

At the end of each of its turns, and each time it takes damage, the target can
make another Wisdom saving throw. The target has advantage on the saving throw
if it’s triggered by damage. On a success, the spell ends.
    """.strip()
    character_class = [classes.Bard, classes.Wizard]
    level = 1
    cast_range = 30
    school = 'Enchantment'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'VSM (tiny tarts and a feather that is waved in the air)'
    concentration = True


class TensersFloatingDisk(Spell):
    name = 'Tenser\'s Floating Disk (Ritual)'
    description = """
This spell creates a circular, horizontal plane of force, 3 feet in diameter
and 1 inch thick, that floats 3 feet above the ground in an unoccupied space of
your choice that you can see within range.
The disk remains for the duration, and can hold up to 500 pounds. If more
weight is placed on it, the spell ends, and everything on the disk falls to the
ground.

The disk is immobile while you are within 20 feet of it. If you move more than
20 feet away from it, the disk follows you so that it remains within 20 feet of
you. It can more across uneven terrain, up or down stairs, slopes and the like,
but it can’t cross an elevation change of 10 feet or more. For example, the
disk can’t move across a 10-foot-deep pit, nor could it leave such a pit if it
was created at the bottom.

If you move more than 100 feet from the disk (typically because it can’t move
around an obstacle to follow you), the spell ends.
    """.strip()
    character_class = [classes.Wizard]
    level = 1
    cast_range = 30
    school = 'Conjuration'
    ritual = True
    casting_time = '1 action'
    duration = 60 * 60
    components = 'VSM (a drop of mercury)'
    concentration = False


class ThunderousSmite(Spell):
    name = 'Thunderous Smite'
    description = """
The first time you hit with a melee weapon attack during this spell’s duration,
your weapon rings with thunder that is audible within 300 feet of you, and the
attack deals an extra 2d6 thunder damage to the target. Additionally, if the
target is a creature, it must succeed on a Strength saving throw or be pushed
10 feet away from you and knocked prone.
    """.strip()
    character_class = [classes.Paladin]
    level = 1
    cast_range = -1
    school = 'Evocation'
    ritual = False
    casting_time = '1 bonus action'
    duration = 60
    components = 'V'
    concentration = True


class Thunderwave(Spell):
    name = 'Thunderwave'
    description = """
A wave of thunderous force sweeps out from you.
Each creature in a 15-foot cube originating from you must make a Constitution
saving throw. On a failed save, a creature takes 2d8 thunder damage and is
pushed 10 feet away from you. On a successful save, the creature takes half as
much damage and isn’t pushed.

In addition, unsecured objects that are completely within the area of effect
are automatically pushed 10 feet away from you by the spell’s effect, and the
spell emits a thunderous boom audible out to 300 feet.

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, the damage
increases by 1d8 for each slot level above 1st.
    """.strip()
    character_class = [
        classes.Bard, classes.Druid, classes.Sorcerer, classes.Wizard
    ]
    level = 1
    cast_range = -1
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 0
    components = 'VS'
    concentration = False


class UnseenServant(Spell):
    name = 'Unseen Servant (Ritual)'
    description = """
This spell creates an invisible, mindless, shapeless force that performs simple
tasks at your command until the spell ends. The servant springs into existence
in an unoccupied space on the ground within range. It has AC 10, 1 hit point,
and a Strength of 2, and it can’t attack. If it drops to 0 hit points, the
spell ends.

Once on each of your turns as a bonus action, you can mentally command the
servant to move up to 15 feet and inteact with an object. The servant can
perform simple tasks that a human servant could do, such as fetching things,
cleaning, mending, folding clothes, lighting fires, serving food, and pouring
wine. Once you give the command, the servant performs the task to the best of
its ability until it completes the task, then waits for your next command.

If you command the servant to perform a task that would move it more than 60
feet away from you, the spell ends.
    """.strip()
    character_class = [classes.Bard, classes.Warlock, classes.Wizard]
    level = 1
    cast_range = 60
    school = 'Conjuration'
    ritual = True
    casting_time = '1 action'
    duration = 60 * 60
    components = 'VSM (a piece of string and a bit of wood)'
    concentration = False


class WitchBolt(Spell):
    name = 'Witch Bolt'
    description = """
A beam of crackling, blue energy lances out toward a creature within range,
forming a sustained arc of lightning between you and the target.
Make a ranged spell attack against that creature. On a hit, the target takes
1d12 lightning damage, and on each of your turns for the duration, you can use
your action to deal 1d12 lightning damage to the target automatically. The
spell ends if you use your action to do anything else. The spell also ends if
the target is ever outside the spell’s range or if it has total cover from you.

~~ At higher level ~~
When you cast this spell using a spell slot of 2nd level or higher, the initial
damage increases by 1d12 for each slot level above 1st.
    """.strip()
    character_class = [classes.Sorcerer, classes.Warlock, classes.Wizard]
    level = 1
    cast_range = 30
    school = 'Evocation'
    ritual = False
    casting_time = '1 action'
    duration = 60
    components = 'VSM (a twig from a tree that has been struck by lightning)'
    concentration = True


class WrathfulSmite(Spell):
    name = 'Wrathful Smite'
    description = """
The next time you hit with a melee weapon attack during this spell’s duration,
your attack deals an extra 1d6 psychic damage.
Additionally, if the target is a creature, it must make a Wisdom saving throw
or be frightened of you until the spell ends. As an action, the creature can
make a Wisdom check against your spell save DC to steel its resolve and end
this spell.
    """.strip()
    character_class = [classes.Paladin]
    level = 1
    cast_range = -1
    school = 'Evocation'
    ritual = False
    casting_time = '1 bonus action'
    duration = 60
    components = 'V'
    concentration = True


class Aid(Spell):
    name = 'Aid'
    description = """
Your spell bolsters your allies with toughness and resolve.
Choose up to three creatures within range. Each target’s hit point maximum and 
current hit points increase by 5 for the duration.

~~ At higher level ~~
When you cast this spell using a spell slot of 3rd level or higher, a target’s 
hit points increase by an additional 5 for each slot level above 2nd.
    """.strip()
    character_class = [classes.Cleric, classes.Paladin]
    level = 2
    cast_range = 30
    school = 'Abjuration'
    ritual = False
    casting_time = '1 round'
    duration = 8 * 60 * 60
    components = 'VSM'
    concentration = False