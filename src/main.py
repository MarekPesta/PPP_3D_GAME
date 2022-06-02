from config import *
from miscellaneous import MyWorld, CubeModifiable
from monster_slayer import MonsterSlayer
from monsters import Unicorn, Monster1, Monster2, Monster3, MonsterGenerator

app = Ursina()
world = MyWorld()
player = MonsterSlayer()
monsterGenerator = MonsterGenerator(player=player)

application.paused = True

Text.size= 50
test = Text(text=f'LVL 0', wordwrap=30, origin=(11, 18))

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


def pause_input(key):
    if key == 'enter':    # press tab to toggle edit/play mode
        application.paused = not application.paused


pause_handler = Entity(ignore_paused=True, input=pause_input)
monsterGenerator.generate(m1=2, m2=2, m3=2)

app.run()
