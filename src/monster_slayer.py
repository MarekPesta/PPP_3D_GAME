from config import *
from weapons import Nufin, Hammer, Rifle


class MonsterSlayer:

    def __init__(self):
        self.controller = FirstPersonController(speed=8, x=-10, z=-10)
        self.hp = None
        self.armory = {'0': Nufin()}
        self.armory.update({'9': Hammer()})
        self.armory.update({'2': Rifle()})
        self.weapon = self.armory['0']

    def change_weapon(self, key: str):
        self.weapon.disable()
        self.weapon = self.armory[key]
        self.weapon.enable()
