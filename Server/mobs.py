# coding=utf-8


class Mob:
    _setm = 0

    mobs = ["Boar", "Wolf", "Bear", "Bandit"]

    mobs_id = {
        "Boar": [50, 50, 10],
        "Wolf": [70, 100, 40],
        "Bear": [120, 230, 100],
        "Bandit": [100, 100, 20],
    }

    def __init__(self):
        self._setm = 0

    @property
    def setm(self):
        return self._setm

    @setm.setter
    def setm(self, id):
        # print "Mob set " + str(id)
        self._setm = id

    def get_name(self):
        return Mob.mobs[self.setm]

    def get_health(self):
        return self.mobs_id[self.mobs[self.setm]][0]

    def get_damage(self):
        return self.mobs_id[self.mobs[self.setm]][1]

    def get_armor(self):
        return self.mobs_id[self.mobs[self.setm]][2]

    def show(self):
        return Mob.mobs[self.setm] + "\n\t\t\tHealth: " + str(self.get_health()) + "\n\t\t\tDamage: " + str(self.get_damage()) + "\n\t\t\tArmor: " + str(self.get_armor())

    @staticmethod
    def print_mobs():
        ss = ""
        i = 0
        for e in Mob.mobs:
            ss += "\t\t" + str(i) + "] " + e + ":\t\t" + str(Mob.mobs_id[e][0]) + "\t" + str(
                Mob.mobs_id[e][1]) + "\n"
            i += 1
        ss += "\n"
        return ss
