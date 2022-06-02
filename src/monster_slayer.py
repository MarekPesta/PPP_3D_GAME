from config import *
from weapons import Nufin, Rifle, Handgun, Railgun  # , Hammer
from ursina.prefabs.health_bar import HealthBar


class MonsterSlayer:

    def __init__(self):
        self.controller = FirstPersonController(model='cube', speed=8, z=-10, origin_y=-.5)
        self.controller.collider = BoxCollider(self.controller, Vec3(0,1,0), Vec3(1,2,1))

        self.hp = 1000
        self.armory = {'0': Nufin()}
        # self.armory.update({'9': Hammer()})
        self.armory.update({'1': Handgun()})
        self.armory.update({'2': Rifle()})
        self.armory.update({'3': Railgun()})
        self.weapon = self.armory['0']

    def change_weapon(self, key: str):
        self.weapon.disable()
        self.weapon = self.armory[key]
        self.weapon.enable()
