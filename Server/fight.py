# coding=utf-8
from tools import *
import knight
import mobs
import collections
import random


def __hit__(_knight, _knight_health, _mob_health):
    _knight_damage = _knight.damage()
    _knight_armor = _knight.armor()
    _knight_parry = _knight.parry()
    _knight_block = _knight.block()
    _knight_dodge = _knight.dodge()
    _mob_damage = _knight.get_mob().get_damage()
    _mob_armor = _knight.get_mob().get_armor()

    _khit = 0
    _mhit = 0

    r = random.randint(4, 7)
    _khit = _knight_damage - r / 100 * _mob_armor
    if _khit < 0:
        _khit = 0
    _mob_health -= _khit
    if _mob_health < 0:
        _mob_health = 0
    else:
        r = random.randint(4, 7)
        if random.random() < _knight_parry / 100:
            pass
        elif random.random() < _knight_block / 100:
            pass
        elif random.random() < _knight_dodge / 100:
            pass
        else:
            _mhit = _mob_damage - r / 100 * _knight_armor
            if _mhit < 0:
                _mhit = 0
            _knight_health -= _mhit
        if _knight_health < 0:
            _knight_health = 0

    # _knight_health -= 10
    # _mob_health -= 10
    # if _mob_health < 0:
    #     _mob_health = 0
    result = (_knight_health, _mob_health, _khit, _mhit)
    return result

