# coding=utf-8
import mobs


class Weapon:
    _setw = 0

    weapons = ["Bare handed", "Sword 1h", "Axe 1h", "Blunt", "Dagger", "Cleaver"]

    weapon_id = {
        "Bare handed": [0, 0],
        "Sword 1h": [100, 40],
        "Axe 1h": [130, 4],
        "Blunt": [60, 20],
        "Dagger": [200, 1],
        "Cleaver": [160, 10]
    }

    def __init__(self):
        self._setw = 0

    @property
    def setw(self):
        return self._setw

    @setw.setter
    def setw(self, id):
        #print "Weapon set " + str(id)
        self._setw = id

    def get_damage(self):
        return self.weapon_id[self.weapons[self.setw]][0]

    def get_parry(self):
        return self.weapon_id[self.weapons[self.setw]][1]

    def show(self):
        return Weapon.weapons[self.setw] + " Damage: " + str(self.get_damage()) + " Parry: " + str(self.get_parry())

    @staticmethod
    def print_weapons():
        ss = ""
        i = 0
        for e in Weapon.weapons:
            ss += "\t\t" + str(i) + "] " + e + ":\t\t" + str(Weapon.weapon_id[e][0]) + "\t" + str(Weapon.weapon_id[e][1]) + "\n"
            i += 1
        ss += "\n"
        return ss


class Armor:
    _seta = 0

    armors = ["Clothes", "Leather Armor", "Chainmail Armor", "Plate Armor"]

    armor_id = {
        "Clothes": [0, 0],
        "Leather Armor": [100, 10],
        "Chainmail Armor": [130, 40],
        "Plate Armor": [260, 90],
    }

    def __init__(self):
        self._seta = 0

    @property
    def seta(self):
        return self._seta

    @seta.setter
    def seta(self, id):
        # print "Armor set " + str(id)
        self._seta = id

    def get_armor(self):
        return self.armor_id[self.armors[self.seta]][0]

    def get_block(self):
        return self.armor_id[self.armors[self.seta]][1]

    def show(self):
        return Armor.armors[self.seta] + " Armor: " + str(self.get_armor()) + " Block: " + str(self.get_block())

    @staticmethod
    def print_armors():
        ss = ""
        i = 0
        for e in Armor.armors:
            ss += "\t\t" + str(i) + "] " + e + ":\t\t" + str(Armor.armor_id[e][0]) + "\t" + str(Armor.armor_id[e][1]) + "\n"
            i += 1
        ss += "\n"
        return ss


class Trinket:
    Strength = 0
    Stamina = 0
    Agility = 0


class Knight:
    Name = ""
    _weapon = Weapon()
    _armor = Armor()
    _trinket = Trinket()
    _statPoints = 7
    _strength = 1
    _stamina = 1
    _agility = 1
    _health = 100
    _mob = mobs.Mob()
    d = (lambda s, x, y, z, w: x + y * z * w)

    def __init__(self, name):
        self.Name = name

    def health(self):
        return self._health + 5 * self._stamina

    def damage(self):
        return self.d(self._strength, self._weapon.get_damage(), 0.7, self._strength)
        #return self._strength + self._weapon.get_damage() * 0.7 * self._strength

    def armor(self):
        return self.d(self._stamina, self._armor.get_armor(), 0.5, self._stamina)
        #return self._stamina + self._armor.get_armor() * 0.7 * self._stamina

    def parry(self):
        return self.d(0, self._agility, 0.4, self._weapon.get_parry())
        #return self._agility * 0.7 * self._weapon.get_parry()

    def block(self):
        return self.d(0, self._armor.get_armor(), 0.3, self._stamina)
        #return self._stamina * 0.7 * self._armor.get_block()

    def dodge(self):
        return self.d(0, self._armor.get_armor(), 0.5, self._stamina)
        #return self._stamina * 0.7 * self._armor.get_block()

    def get_weapon(self):
        return self._weapon

    def get_armor(self):
        return self._armor

    def get_stat_points(self):
        return self._statPoints

    def set_stat_points(self, stat):
        self._statPoints = stat

    def get_strength(self):
        return self._strength

    def set_strength(self, stat):
        self._strength = stat

    def get_stamina(self):
        return self._stamina

    def set_stamina(self, stat):
        self._stamina = stat

    def get_agility(self):
        return self._agility

    def set_agility(self, stat):
        self._agility = stat

    def get_mob(self):
        return self._mob
