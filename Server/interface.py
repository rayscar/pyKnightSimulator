# coding=utf-8
from tools import *
import knight
import mobs


def __main_menu__(_knight):
    ss = "\tSUMMARY:\n"
    ss += "\t\tHealth:\t" + str(_knight.health()) + "\n"
    ss += "\t\tDamage:\t" + str(_knight.damage()) + "\n"
    ss += "\t\tArmor:\t" + str(_knight.armor()) + "\n"
    ss += "\t\tParry:\t" + str(_knight.parry()) + "\n"
    ss += "\t\tBlock:\t" + str(_knight.block()) + "\n"
    #ss += "\t\tDodge:\t\n" + str(_knight.dodge()) + "\n"

    ss += "\n\tMENU:\n"

    ss += "\t\t1] Stats\n"
    ss += "\t\t2] Equipment\n"
    ss += "\t\t3] Mission\n"

    return ss


def __stats__(_knight):
    ss = "\tSTATS:\n"
    ss += "\tStat Point: " + str(_knight.get_stat_points()) + "\n"
    ss += "\t\t1] Strength:\t" + str(_knight.get_strength()) + "\n"
    ss += "\t\t2] Stamina:\t" + str(_knight.get_stamina()) + "\n"
    ss += "\t\t3] Agility:\t" + str(_knight.get_agility()) + "\n"
    ss += "\t\tB] Back\n"

    return ss


def __equipment__(_knight):
    ss = "\tEQUIPMENT:\n"

    ss += "\t\tWeapon:\t" + str(_knight.get_weapon().show()) + "\n"
    ss += "\t\tArmor:\t" + str(_knight.get_armor().show()) + "\n\n"
    #ss += "\t\tTrinket:\t\n"

    ss += "\t\t1] Change Weapon:\t\n"
    ss += "\t\t2] Change Armor:\t\n"
    ss += "\t\t3] Change Trinket:\t\n"
    ss += "\t\tB] Back\n"

    return ss


def __change_weapon__(_knight):
    ss = "\tCHANGE WEAPON:\n"
    ss += knight.Weapon.print_weapons()
    ss += "\t\tChoose your Weapon:\t"

    return ss


def __change_armor__(_knight):
    ss = "\tCHANGE ARMOR:\n"
    ss += knight.Armor.print_armors()
    ss += "\t\tChoose your Armor:\t"

    return ss


def __change_trinket__(_knight):
    pass


def __mission__(_knight):
    ss = "\tMission:\n"

    ss += "\t\tMob: " + str(_knight.get_mob().show()) + "\n\n"

    ss += "\t\t1] Change Mob:\t\n"
    ss += "\t\t2] Simulate fight\t\n"
    ss += "\t\tB] Back\n"

    return ss


def __change_mob__(_knight):
    ss = "\tCHANGE MOB:\n"
    ss += mobs.Mob.print_mobs()
    ss += "\t\tChoose Mob you want to fight:\t"

    return ss


def __sim_fight__(_knight, _knight_health, _mob_health, _khit, _mhit):
    ss = "\tYou hit with: " + str(_khit) + " damage\n"
    ss += "\t" + str(_knight.get_mob().get_name()) + " hits with: " + str(_mhit) + " damage\n"
    ss += "\tYour health: " + str(_knight_health)
    ss += ",  \t" + str(_knight.get_mob().get_name()) + "'s health: " + str(_mob_health) + "\n"

    if _knight_health == 0:
        ss += "\nYou LOSE!"
    elif _mob_health == 0:
        ss += "\nYou WIN!"

    return ss
