"""Module to create and manage a Character in DnD.

https://media.wizards.com/2016/dnd/downloads/5E_CharacterSheet_Fillable.pdf

https://www.dndbeyond.com/sources/basic-rules/step-by-step-characters
"""

import os
import random
from typing import Dict, List, Tuple

from dnd.dice import DiceBag
from dnd.races.languages import Language, ClassHandler as language_handler
from dnd.races.sizes import Size, ClassHandler as size_handler
from dnd.skills import Skill, ClassHandler as skill_handler
from dnd.troubleshoot import debug


LEVEL = [
    {'xp': 0, 'proficiency_bonus': 0},      #Level 0
    {'xp': 300, 'proficiency_bonus': 2},    #Level 1
    {'xp': 900, 'proficiency_bonus': 2},    #Level 2
    {'xp': 2700, 'proficiency_bonus': 2},   #Level 3
    {'xp': 6500, 'proficiency_bonus': 2},   #Level 4
    {'xp': 14000, 'proficiency_bonus': 3},  #Level 5
    {'xp': 23000, 'proficiency_bonus': 3},  #Level 6
    {'xp': 34000, 'proficiency_bonus': 3},  #Level 7
    {'xp': 48000, 'proficiency_bonus': 3},  #Level 8
    {'xp': 64000, 'proficiency_bonus': 4},  #Level 9
    {'xp': 85000, 'proficiency_bonus': 4},  #Level 10
    {'xp': 100000, 'proficiency_bonus': 4}, #Level 11
    {'xp': 120000, 'proficiency_bonus': 4}, #Level 12
    {'xp': 140000, 'proficiency_bonus': 5}, #Level 13
    {'xp': 165000, 'proficiency_bonus': 5}, #Level 14
    {'xp': 195000, 'proficiency_bonus': 5}, #Level 15
    {'xp': 225000, 'proficiency_bonus': 5}, #Level 16
    {'xp': 265000, 'proficiency_bonus': 6}, #Level 17
    {'xp': 305000, 'proficiency_bonus': 6}, #Level 18
    {'xp': 355000, 'proficiency_bonus': 6}, #Level 19
    {'xp': 999999, 'proficiency_bonus': 6}, #Level 20
]

def proficiency_bonus(level: int) -> int:
    """Calculate proficiency bonus based on level"""
    return int((level + 7) / 4)

def ability_modifier(score: int) -> int:
    """Calculate ability modifier based on ability score"""
    return int((score - score % 2) / 2) - 5

def header(title) -> str:
    """Takes a title and turns it into a Header in the followinng form:

    ======================
    === EXAMPLE HEADER ===
    ======================

    Parameters
    ----------
    title : str
        Title to go in Header
    """
    title = f'~~~ {title.upper()} ~~~'
    bar = '~' * len(title)
    return f'{bar}\n{title}\n{bar}'

def equipment_weight(equipment) -> float:
    """Calculate the total weight of equipment
        
    Parameters
    ----------
    equipment : List[object]
        List of the equipment to be weighed

    Returns
    -------
    total : float
        Total weight of equipment
    """
    total = 0
    for item in equipment:
        try:
            if type(item) == type:
                total += item.base_weight
            elif type(item) == list:
                total += equipment_weight(item)
            else:
                total += item.weight
        except:
                continue
    return total

def stringify(obj) -> str:
    """Turn an object into a string
    
    Args
    ----
    obj : object
        - Could be object of type str, list, dict, or dnd class. 
        - If arg type is str, then string is updated to a dict and function
        is called again with dict obj as arg.
        - If arg type is list, then each element in the list has the function
        run on it resulting in a list of strings, which is then joined with
        comma. This new string is then sent as arg to function.
        - If arg type is dict, then the dict is converted to a list of str and
        then this list is joined to a string.
        - If arg type is anything else, then it is presumed to be of a class
        from the dnd module.  The function is then called again on the name
        variable which is of type str.

    Returns
    -------
    to_string : str
        The final string representation.
    """
    if type(obj) == str:
        _all = obj.split(', ')
        _d = {}
        for _o in _all:
            if _o not in _d:
                _d[_o] = 0
            _d[_o] += 1
        to_string = stringify(_d)
    elif type(obj) == list:
        to_string = stringify(', '.join([stringify(_o) for _o in obj]))
    elif type(obj) == dict:
        _to_list = [f'{k} x{v}' if v > 1 else f'{k}' for k, v in obj.items()]
        to_string = ', '.join(_to_list)
    else:
        to_string = stringify(obj.name)
    
    return to_string


class Character:
    """Base class for generic Character.
    
        The idea at this time is this class will basically mimic a 5e Character
    sheet.  This class will go through many revisions to work properly, I 
    believe.
        Plan is to randomize (roll) for all details which are not
    provided manually.  Currently require name, sex, race, starting_class,
    and alignment.

    Input Parameters
    ----------
    name : str
        The name of the Character.
    sex : str
        Sex of Character (`Male` or `Female`)
    age : int
        Age of Character
    race : races.CharacterRace
        Race of Character.
    starting_class : classes.CharacterClass
        Starting Class of Character.
    alignment : alignments.Alignment
        Alignment of character.  If left None, then an alignment will be chosen
        from a list based on Race/Class.
    randomize : bool (Default: True)
        Whether all character choices will be randomly rolled for
    
    Derived Parameters
    ------------------
    height : int
        Height, in inches.  If not provided, will be derived from Race.
    weight : int
        Weight, in pounds.  If not provided, will be derived from Race.
    xp : int
        Experience points, used to determine level.
    level : int
        Character's total level.  This is based on the current xp.
    proficiency_bonus : int
        Bonus added to rolls in which Character has proficiency.  Based solely
        on Character level (not Class level).
    base_ability_modifier : Dict[str, int]
        Modifiers to add or subtract from rolls.  Based on ability scores.
    saving_throws : Dict[str, bool]
        Dict to indicate which saving throws the Character has proficiency.  
        Will be derived from Character Race/Class/Feats.
    skills : List[skills.Skill]
        Skills the Character has proficiency in.  Derived from Race/Class, as
        well as chosen by player at level-up.

    User Defined Parameters
    -----------------------
    classes : List[Tuple(classes.CharacterClass, int)]
        Class and Class level of the Character.  #TODO: Multi-classing
    base_ability : Dict[str, int]
        The characters base stats e.g. `STR` and `CON`.  Modified during
        Character level-up.
    """
    def __init__(self,
                 name: str,
                 sex: str,
                 race,
                 starting_class,
                 alignment,
                 background,
                 height: int,
                 weight: int,
                 randomize: bool = False,
                 ) -> None:
        """Initialize Character"""
        self.race = race
        self.sex = sex
        self.name = name
        self.classes = [(starting_class, 0)]
        self.alignment = alignment
        self.background = background
        self.height = height
        self.weight = weight
        self.randomize = randomize
        
        self.xp = 1200
        self.level = 0
        self.initiative_bonus = 0
        self.hit_points_max = 0
        self.hit_points = 0
        self.hit_dice = []
        self.temp_hit_points = 0
        self.base_speed = self.race.base_speed
        self.saving_throws = starting_class.saving_throws
        self.inspiration = 0

        self.skills = []
        self.languages = []
        self.features = []
        self.traits = []

        self.base_ability = {
            'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'WIS': 0, 'CHA': 0
        }
        self.base_ability_modifier = {
            'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'WIS': 0, 'CHA': 0
        }
        self.ability_bonus = {
            'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'WIS': 0, 'CHA': 0
        }
        self.equipment = {
            'Adventuring Gear': [],
            'Armor': [],
            'Equipment Pack': [],
            'Mount': [],
            'Tool': [],
            'Weapon': [],
            'Other': [],
        }
        self.proficiencies = {
            'Armor': [],
            'Tool': [],
            'Weapon': [],
            'Languages': self.languages,
            'Other': [],
        }
        self.equipped = {
            'Adventuring Gear': [],
            'Armor': [],
            'Tool': [],
            'Weapon': [],
            'Other': [],
        }

        title = '== Adding Racial traits... =='
        self._level_up_commands(self.race.traits, title=title)
        title = '== Adding Background traits... =='
        self._level_up_commands(self.background.traits, title=title)
        self.characteristics = {}
        for k, v in self.background.characteristics.items():
            title = f'== Choose {k.title()} =='
            self.characteristics[k.title()] = self.choose(v, title=title)[0]
        self._roll_for_base_abilities()
        title = '== Adding Class lvl 0 traits...'
        self._level_up_commands(self.classes[0][0].level[0])
      
        while self._check_lvlup():
            self.level_up()
        self.can_level = False

        self._equip_armor()
        self._equip_weapon()
        self._equip_gear()

        #TODO: A lot more shit...

    def __str__(self) -> str:
        """Return a string representation of the Character"""
        return '\n'.join([
            f'Name:       {self.name}',
            f'Race:       {self.race.name}',
            f'Class:      {self._pretty_classes()}',
            f'Background: {self.background.name}',
            f'Alignment:  {self.alignment.name}',
            f'Sex:        {self.sex}',
            f'Height:     {int(self.height / 12)}\'{self.height % 12}"',
            f'Weight:     {self.weight} lbs',
        ])

    def __repr__(self) -> str:
        return f''   

    def sheet(self) -> str:
        """Returns full character sheet in str format"""
        return '\n'.join([
            header('character sheet'),
            self._pretty_character_info(),
            header('personality traits'),
            self._pretty_traits(),
            header('vitals'),
            self._pretty_vitals(),
            header('ability scores'),
            self._pretty_ability(),
            header('proficiencies'),
            self._pretty_proficiency(),
            header('skills, features, and traits'),
            self._pretty_skills(),
            header('equipment'),
            f'~~~ Equipped ~~~',
            self._pretty_equipped(),
            f'\n~~~ Unequipped ~~~',
            self._pretty_equipment(),
        ])

    def _pretty_character_info(self) -> str:
        """Returns string of vital stats"""
        return '\n'.join([
            f'Name:       {self.name}',
            f'Race:       {self.race.name}',
            f'Class:      {self._pretty_classes()}',
            f'Background: {self.background.name}', 
            f'Sex:        {self.sex}',
            f'Height:     {int(self.height / 12)}\'{self.height % 12}"',
            f'Weight:     {self.weight}',
            f'Exp Points: {self.xp}',
        ])

    def _pretty_traits(self) -> str:
        """Return str representation of characteristics"""
        max_key_len = sorted([len(i) for i in self.characteristics.keys()])[-1]
        out = []
        for k, v in self.characteristics.items():
            spaces = ' ' * (max_key_len - len(k) + 1)
            out.append(f'{k}:{spaces}{v}')
        return '\n'.join(out)

    def _pretty_vitals(self) -> str:
        """Returns string of vital stats

        XP, Level, Armor Class, Initiative, HP Max, Current HP
        """
        return '\n'.join([
            f'Inspiration:       {self.inspiration}',
            f'Proficiency Bonus: {self._proficiency_bonus()}',
            f'Armor Class:       {self.armor_class()}',
            f'Initiative:        {self.initiative_bonus}',
            f'Speed:             {self.base_speed}',
            f'Hit Points:        {self.hit_points} / {self.hit_points_max}',
            f'Temp Hit Points:   {self.temp_hit_points}',
            f'Hit Dice:          {", ".join(self.hit_dice)}',
            f'Max Hit Dice:      {", ".join(self._max_hit_dice())}',
            f'Carry Capacity:    {self._carry_capacity()}',
            f'Weight Carried:    {self._carry_weight()}',
        ])

    def _pretty_classes(self) -> str:
        """String of self.classes"""
        return ', '.join([f'Level {l} {c.name}' for c, l in self.classes])

    def _pretty_skills(self) -> str:
        """String of skills"""
        return '\n'.join([
            f'Skills:        {stringify(self.skills)}',
            f'Features:      {stringify(self.features)}',
            f'Traits:        {stringify(self.traits)}',
            f'Saving Throws: {", ".join(self.saving_throws)}',
        ])

    def _pretty_ability(self) -> str:
        """Returns string of Ablility stats"""
        out = []
        for ability, score in self.base_ability.items():
            total_score = self.ability_score(ability)
            bonus = self.ability_bonus[ability]
            mod = self._ability_modifier(ability)
            bonus = f'0{bonus}' if bonus and bonus < 10 else bonus
            total_score = f'0{score}' if score < 10 else score
            mod = f'+{mod}' if mod >= 0 else f'{mod}'
            if bonus:
                line = f'{ability}: {total_score} ({bonus}) [{mod}]'
            else:
                line = f'{ability}: {total_score}      [{mod}]'
            out.append(line)
        return '\n'.join(out)

    def _pretty_proficiency(self) -> str:
        out = []
        key_lengths = [
            len(k) if v else 0 for k, v in self.proficiencies.items()
        ]
        max_key_len = sorted(key_lengths)[-1]
        for k, v in self.proficiencies.items():
            if v:
                items = stringify(v)
                spaces = ' ' * (max_key_len - len(k) + 1)
                out.append(f'{k}:{spaces}{items}')
        return '\n'.join(out)

    def _pretty_equipment(self) -> str:
        out = []
        key_lengths = [len(k) if v else 0 for k, v in self.equipment.items()]
        max_key_len = sorted(key_lengths)[-1]
        for k, v in self.equipment.items():
            if v:
                items = stringify(v)
                spaces = ' ' * (max_key_len - len(k) + 1)
                out.append(f'{k}:{spaces}{items}')
        return '\n'.join(out)

    def _pretty_equipped(self) -> str:
        out = []
        key_lengths = [len(k) if v else 0 for k, v in self.equipped.items()]
        max_key_len = sorted(key_lengths)[-1]
        for k, v in self.equipped.items():
            if v:
                items = stringify(v)
                spaces = ' ' * (max_key_len - len(k) + 1)
                out.append(f'{k}:{spaces}{items}')
        return '\n'.join(out)

    def get_func(self, name: str):
        funcs = {
            'add_base_ability_points': self.add_base_ability_points,
            'add_equipment': self.add_equipment,
            'add_feats': self.add_feats,
            'add_languages': self.add_languages,
            'add_proficiencies': self.add_proficiencies,
            'add_saving_throws': self.add_saving_throws,
            'add_skills': self.add_skills,
            'add_traits': self.add_traits,
            'choose_ability_points': self.choose_ability_points,
            'choose_cantrips': self.choose_cantrips,
            'choose_equipment': self.choose_equipment,
            'choose_language': self.choose_language,
            'choose_proficiencies': self.choose_proficiencies,
            'choose_skills': self.choose_skills,
        }
        return funcs.get(name)

    def full_character_sheet(self) -> str:
        """Returns a string representation of entire character sheet"""
        return '\n'.join([
            f'{self.name}',
            f'{self.race.name}',
            f'{self.sex}',
            f'{int(self.height / 12)}\'{self.height % 12}" {self.weight}lbs', 
            f'{self.alignment.name}',
            ', '.join([f'Level {l} {c.name}' for c, l in self.classes]),
            f'Experience Points: {self.xp}',
            f'\nABILITIES:\n{self._pretty_ability}',

        ])

    def equip_item(self, item_type=''):
        """Ask player what type of item to equip and call corresponding func"""
        funcs = {
            'armor': self._equip_armor,
            'weapon': self._equip_weapon,
            'gear': self._equip_gear,
        }
        options = [k.capitalize() for k in list(funcs.keys())]
        if not item_type or item_type not in options:
            title = '=== Choose Equipment Type to Equip ==='
            item_type = self.choose(options, title=title)
        func = funcs[item_type.lower]
        func()

    def _equip_armor(self):
        options = self.equipment['Armor']
        equipped = self.equipped['Armor']
        while len(options) > 0:
            str_equipped = f'Currently Equipped: {stringify(equipped)}'
            title = f'=== Choose Armor to Equip ===\n{str_equipped}'
            item = self.choose(options + ['END'], title=title)[0]
            if item == 'END':
                break
            for _eq in equipped:
                if ('Armor' in _eq.item_type and 'Armor' in item.item_type
                        or _eq.item_type == item.item_type):
                    _r = equipped.pop(equipped.index(_eq))
                    options.append(_r)
                    break
            equipped.append(item)
            options.pop(options.index(item))

    def _equip_weapon(self):
        options = self.equipment['Weapon']
        equipped = self.equipped['Weapon']
        while len(options) > 0:
            str_equipped = f'Currently Equipped: {stringify(equipped)}'
            title = f'=== Choose Weapon to Equip ===\n{str_equipped}'
            item = self.choose(options + ['END'], title=title)[0]
            if item == 'END':
                break
            if equipped:
                _r = equipped.pop(0)
                options.append(_r)
            equipped.append(item)
            options.pop(options.index(item))

    def _equip_gear(self):
        pass

    def _carry_weight(self):
        """Calculates and returns the total weight of carried equipment"""
        _values = list(self.equipped.values()) + list(self.equipment.values())
        items = []
        for _v in _values:
            items += _v
        return equipment_weight(items)

    def _carry_capacity(self) -> int:
        """Calculate the carry capacity in lbs of character"""
        return self.base_ability['STR'] * 15

    def _roll_height_weight(self) -> None:
        """Set Character Height and Weight"""
        self.height, self.weight = roll_height_weight(self.race)

    def _check_lvlup(self) -> bool:
        """Check if current xp is enough to level up"""
        return self.xp >= LEVEL[self.level]['xp']

    def level_up(self) -> None:
        """Level up the character"""
        self.level += 1
        #No multiclassing at this time
        _cls, _lvl = self.classes[0]
        _lvl += 1
        self.classes[0] = (_cls, _lvl)
        title = f'=== Advancing to Level {_lvl} {_cls.name}! ==='
        self._level_up_commands(_cls.level[_lvl], title=title)

        #Roll hit-die for HP
        cheat = True if _lvl == 1 else False
        roll = self.roll_hit_die(_cls.hit_die, cheat=cheat)
        self.hit_points_max += roll
        self.hit_points = self.hit_points_max
        self.hit_dice = self._max_hit_dice()

    def _level_up_commands(self, funcs, title='') -> None:
        """Runs the functions provided in funcs

        Parameters
        ----------
        funcs : Dict[str, object]
            function name and parameters to use in function
        title : str
            Optional title to print before running commands
        """
        if not self.randomize and title:
            os.system('clear')
            print(title)
            input(f'Press Enter to Continue...')
        for name, params in funcs:
            func = self.get_func(name)
            func(**params)

    def choose(self, options, num=1, unique=False, title=''):
        """Choose from provided options

        Parameters
        ----------
        options : list[object]
            List of choices
        num : int
            Number of choices
        unique : bool
            If True, then each option is removed from choices after chosen
        title : str
            Title to print for user; e.g. `== Choose Weapon ==`

        Returns
        -------
        choices : list[object]
            List of chosen objects
        """
        if num >= len(options) and unique:
            return options
        str_opts = [stringify(_o) for _o in options]
        str_choices = []
        choices = []
        while num > 0:
            _opts = '\n'.join(
                [f'{i}: {str_opts[i]}' for i in range(len(str_opts))]
            )
            if self.randomize:
                _i = random.randrange(0, len(options))
            else:
                _i = -1
                tries = 0
                while _i not in range(len(str_opts)) and tries < 5:
                    os.system('clear')
                    print(title)
                    if str_choices:
                        print(f'Previous Choices: {", ".join(str_choices)}')
                    if num > 1:
                        print(f'Remaining choices: {num}')
                    print(_opts)
                    try:
                        _i = int(input('Choice: '))
                    except:
                        tries += 1
                        continue
            choices.append(options[_i])
            str_choices.append(str_opts[_i])
            if unique:
                options.pop(_i)
                str_opts.pop(_i)
            num -= 1
        return choices

    def roll_dice(self, dice, ability='', proficiency=False, **kwargs) -> int:
        """The basis of DnD, rolling dice!

        Parameters
        ----------
        dice : str
            Number and type of dice to roll, in format `2d6`, `1d20`
        ability : str
            (Optional) Ability modifier to add to total.
        proficiency : bool
            Whether to check for proficiency bonus.

        Returns
        -------
        total : int
            The value of all dice rolled
        """
        if not self.randomize:
            print(f'Rolling {stringify(dice)}...')
            kwargs['show'] = True
        roll = DiceBag.roll_dice(dice, **kwargs)
        ability_mod = self._ability_modifier(ability) if ability else 0
        if ability_mod and not self.randomize:
            print(f'{ability} mod: +{ability_mod}')
        if proficiency and ability in self.saving_throws:
            prof_bonus = self._proficiency_bonus()
            if not self.randomize:
                print(f'Proficiency Bonus: +{prof_bonus}')
        else:
            prof_bonus = 0            
        return roll + ability_mod + prof_bonus

    def _ability_modifier(self, ability: str = '') -> int:
        """Calculates ability modifier to add to roll"""
        score = self.ability_score(ability)
        return ability_modifier(score)

    def armor_class(self) -> int:
        """Calculates and returns Armor Class"""
        char_dex_mod = self._ability_modifier('DEX')
        armor = self.equipped['Armor']
        if not armor:
            return 10 + char_dex_mod
        ac = 0
        for item in armor:
            if item.item_type == 'Shield':
                ac += 2
            else:
                ac += item.armor_class
                ac += sorted([char_dex_mod, item.dex_mod])[0]
        return ac

    def ability_score(self, ability: str) -> int:
        """Calculates total Ability Score which is the sum of the base score
        and any bonuses.

        Parameters
        ----------
        ability: Ability to check score

        Returns
        -------
        score: Total ability score
        """
        return self.base_ability.get(ability) + self.ability_bonus.get(ability)

    def _proficiency_bonus(self) -> int:
        """Calculates current proficiency bonus based on character level"""
        return proficiency_bonus(self.level)

    def roll_hit_die(self, hit_die='', **kwargs) -> int:
        """Roll a hit_die and return value

        Parameters
        ----------
        hit_die : str
            Hit die to roll e.g `1d8` or `1d6` (based on class)
        cheat : bool
            Whether to roll max-value, such as first level of class.

        Returns
        -------
        total: Result of the roll
        """
        if not hit_die:
            title = '=== Choose a Hit Die ==='
            options = DiceBag.grab_dice(self.hit_dice)
            hit_die = self.choose(options, title=title)
        if not self.randomize:
            print(f'=== Roll Hit Dice ===')
            input('Press Enter to continue...')
        return self.roll_dice(hit_die, ability='CON', **kwargs)

    def _max_hit_dice(self) -> List[str]:
        """Get the current available hit die for character level"""
        hit_dice = {}
        for _cls, _lvl in self.classes:
            _die = _cls.hit_die[1:]
            if _die not in hit_dice:
                hit_dice[_die] = 0
            hit_dice[_die] += _lvl
        return [f'{v}{k}' for k, v in hit_dice.items()]

    def _roll_for_base_abilities(self) -> None:
        """Roll for initial base abilities"""
        params = {'dice': '4d6', 'drop_low': True, 'reroll_ones': True}
        if self.randomize:
            for ability in self.base_ability.keys():
                self.add_base_ability_points(ability, self.roll_dice(**params))
        else:
            params['show'] = True
            os.system('clear')
            print(f'=== Roll for Ability Points ===')
            input('Press Enter to roll stats...')
            scores = [self.roll_dice(**params) for _ in range(6)]
            scores.sort(reverse=True)
            print(f'Scores: {" ".join([str(s) for s in scores])}')
            input('Press Enter to continue...')
            abilities = list(self.base_ability.keys())
            for score in scores:
                choice = self.choose_ability_points(abilities, points=score)
                for k in choice.keys():
                    abilities.pop(abilities.index(k))

    def choose_ability_points(self, 
                              options: List[str],
                              num: int = 1,
                              points: int = 1,
                              unique: bool = False) -> dict:
        """Choose an ability to add points.  If num is equal to or greater than
        options, then all options will be added.

        Parameters
        ----------
        num : int
            Number of abilities to choose
        options : List[str]
            Available abilities to choose from
        unique : bool
            Whether or not the same ability can be chosen multiple times

        Returns
        -------
        choices : dict
            Dict of choices made; e.g. {'STR': 4, 'DEX': 1}
        """
        choices = {}
        _opts = [opt for opt in options if self.base_ability[opt] < 20]
        print(_opts)
        while num > 0:
            _curr_scores = " | ".join(
                [f'{k}: {v}' for k, v in self.base_ability.items()]
            )
            title = f'CHOOSE ABILITY - Points: {points} - {_curr_scores}'
            _abl = self.choose(_opts, title=title)
            for choice in _abl:
                if choice not in choices:
                    choices[choice] = 0
                spent = self.add_base_ability_points(choice, points)
                choices[choice] += spent
            num -= 1
            if unique or self.base_ability[choice] >= 20:
                _opts.pop(_opts.index(choice))
        return choices

    def add_base_ability_points(self, ability: str, points: int) -> int:
        """Add points to base_ability.  Maximum for any ability is 20.
        
        Parameters:
        -----------
        ability : str
            Ability getting updated
        points : int
            Number of points to try and add

        Return
        ------
        spent : int
            Total of points spent
        """
        spent = 0
        while points > 0 and self._add_base_ability_point(ability):
            points -= 1
            spent += 1
        return spent

    def _add_base_ability_point(self, ability: str) -> bool:
        """Attempt to add one point to base ability"""
        if self.base_ability[ability] < 20:
            self.base_ability[ability] += 1
            return True
        return False

    def choose_language(self, options, num=1) -> None:
        """Choose a language to learn.  If num is equal to or greater than
        options, then all options will be added.

        Parameters
        ----------
        options : List[dnd.races.languages.Language]
            Available languages to choose from
        num : int
            Number of languages to choose
        """
        _opts = [opt for opt in options if opt not in self.languages]
        known = ', '.join([l.name for l in self.languages])
        title = '\n'.join([
            '=== Choose Language ===',
            f'Known: {known}',
        ])
        self.add_languages(
            self.choose(_opts, num=num, title=title, unique=True)
        )

    def add_languages(self, languages) -> None:
        """Add languages to known list"""
        for language in languages:
            self._add_language(language)

    def _add_language(self, language) -> None:
        if language not in self.languages:
            self.languages.append(language)

    def add_saving_throws(self, abilities: List[str]) -> None:
        for ability in abilities:
            self._add_saving_throw(ability)

    def _add_saving_throw(self, ability: str) -> None:
        self.saving_throws[ability] = True

    def choose_traits(self, options, num=1) -> None:
        """Choose Traits to be proficient in.  If num is equal to or greater
        than options, then all options will be added.

        Parameters
        ----------
        options : List[str]
            Available traits to choose from
        num : int
            Number of traits to choose
        """
        _opts = [opt for opt in options if opt not in self.traits]
        known = ', '.join([t.name for t in self.traits])
        title = '\n'.join([
            '=== Choose Trait ===',
            f'Known: {known}',
        ])
        self.add_traits(self.choose(_opts, num=num, unique=True, title=title))

    def add_traits(self, traits: List[str]) -> None:
        """Add multiple traits"""
        for trait in traits:
            self._add_trait(trait)

    def _add_trait(self, trait: str) -> bool:
        if trait not in self.traits:
            self.traits.append(trait)
            return True
        return False

    def choose_cantrips(self, options, num=1) -> None:
        """Choose cantrips to learn.  If num is equal to or greater
        than options, then all options will be added.

        Parameters
        ----------
        options : List[str]
            Available options to choose from
        num : int
            Number of proficiencies to choose
        """
        pass

    def choose_feats(self, options, num=1) -> None:
        """Choose feats to learn.  If num is equal to or greater
        than options, then all options will be added.

        Parameters
        ----------
        options : list
            Available options to choose from
        num : int
            Number of proficiencies to choose
        """
        _opts = [opt for opt in options if opt not in self.features]
        known = ', '.join([t.name for t in self.features])
        title = '\n'.join([
            '=== Choose Feat ===',
            f'Known: {known}',
        ])
        self.add_feats(self.choose(_opts, num=num, unique=True, title=title))

    def add_feats(self, feats: list) -> None:
        for feat in feats:
            self._add_feat(feat)

    def _add_feat(self, feat: str) -> bool:
        if feat not in self.features:
            self.features.append(feat)
            return True
        return False

    def choose_equipment(self, options, num=1, unique=False):
        title = '=== Choose Equipment ==='
        self.add_equipment(
            self.choose(options, num=num, unique=unique, title=title)
        )

    def add_equipment(self, items):
        if isinstance(items, list):
            for _i in items:
                self.add_equipment(_i)
        elif isinstance(items, dict):
            for item, num in items.items():
                self.add_equipment(num * [item])
        elif isinstance(items, tuple):
            item, kwargs = items
            self._add_equipment(item, **kwargs)
        else:
            self._add_equipment(items)

    def _add_equipment(self, item, **kwargs):
        try:
            if type(item) == type:
                item = item(**kwargs)
            base_type = 'Other' if type(item) == str else item.base_type
            self.equipment[base_type].append(item)
        except Exception as err:
            self.equipment['Other'].append(item)
            print(f'ERROR: _add_equipment() - {err}')
            
    def choose_skills(self, options, num=1):
        _opts = [opt for opt in options if opt not in self.skills]
        title = '=== Choose Skill ==='
        self.add_skills(self.choose(_opts, num=num, unique=True, title=title))

    def add_skills(self, skills):
        if isinstance(skills, list):
            for _i in skills:
                self.add_skills(_i)
        else:
            self._add_skill(skills)

    def _add_skill(self, skill):
        try:
            if isinstance(skill(), Skill) and skill not in self.skills:
                self.skills.append(skill)
        except Exception as err:
            print(f'ERROR: _add_skill() - {err}')

    def choose_proficiencies(self, options, num=1):
        _opts = []
        for _opt in options:
            _b = _opt.base_type
            _v = self.proficiencies.get(_b, self.proficiencies['Other'])
            if _opt not in _v:
                _opts.append(_opt)
        title = '=== Choose Proficiency ==='
        self.add_proficiencies(
            self.choose(_opts, num=num, unique=True, title=title)
        )

    def add_proficiencies(self, items):
        if isinstance(items, list):
            for _p in items:
                self.add_proficiencies(_p)
        else:
            self._add_proficiency(items)

    def _add_proficiency(self, item):
        try:
            _b = item.base_type if type(item) == type else 'Other'
            _v = self.proficiencies.get(_b, self.proficiencies['Other'])
            if item not in _v:
                _v.append(item)
        except Exception as err:
            print(f'_add_proficiency() - {err}')