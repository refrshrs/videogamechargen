#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice

from PillarsRace import SUBRACES, ALL_SUBRACES, RACES
from PillarsAttribute import ATTRIBUTES, STAT_BLOCK
from PillarsSkill import SKILL_BLOCK
from PillarsClass import choice_class_exception_resolver, CLASSES, PClass_Wizard

class Character:
    def __init__(self, name):
        self.name = name
        self.gender = None
        self.race = None
        self.subrace = None
        self.char_class = None
        self.char_class_extra = {}
        self.attributes = STAT_BLOCK
        self.skills = SKILL_BLOCK


def gen_race(c: Character, race: str = None):
    if race is None or race not in ['Human', 'Aumauna', 'Dwarf', 'Elf', 'Orlan', 'Godlike']:
        r = choice(ALL_SUBRACES)
    else:
        r = choice(SUBRACES[race])
    print(r.subrace_name)

def gen_class(c: Character):
    cl = choice(CLASSES)
    c.char_class = cl
    c.char_class_extra = choice_class_exception_resolver(cl.name, c)

jerry = Character('Jerry')
print(jerry.attributes.might)
print(jerry.skills.athletics)

gen_class(jerry)

print(jerry.char_class)
print(jerry.char_class_extra)