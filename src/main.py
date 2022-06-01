from config import *
from miscellaneous import MyWorld, CubeModifiable
from monster_slayer import MonsterSlayer

app = Ursina()
world = MyWorld()
player = MonsterSlayer()


def input(key):
    if key == "escape":
        quit()

    if key == 'left mouse down':
        player.weapon.single_action()

    if key in player.armory:
        player.change_weapon(key)


def update():
    if held_keys['left shift']:
        player.controller.speed = 20
    else:
        player.controller.speed = 8

    if held_keys['left mouse']:
        player.weapon.multi_action()

#gun = Entity(model='cube', parent=camera, position=(.5,-.25,.25), scale=(.3,.2,1), origin_z=-.5, color=color.red, on_cooldown=False)
#gun.muzzle_flash = Entity(parent=gun, z=1, world_scale=.5, model='quad', color=color.yellow, enabled=False)


app.run()
