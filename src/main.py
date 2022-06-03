from config import *
from miscellaneous import MyWorld, CubeModifiable
from monster_slayer import MonsterSlayer
from monsters import Unicorn, Monster1, Monster2, Monster3, MonsterGenerator

app = Ursina()
world = MyWorld()
player = MonsterSlayer()
monsterGenerator = MonsterGenerator(player=player)

application.paused = True

first_text = Text(text=f'Press ENTER to start', scale=1, x=-0.1, y=0.1)


def input(key):
    if key == "escape":
        quit()

    if key == 'left mouse down':
        player.weapon.single_action()

    if key in player.armory:
        player.change_weapon(key)

    if key == 'g':
        monsterGenerator.generate(m1=2, m2=2, m3=2)


def update():
    if held_keys['left shift']:
        player.controller.speed = 20
    else:
        player.controller.speed = 8

    if held_keys['left mouse']:
        player.weapon.multi_action()

    if len(monsterGenerator.enemies) == 0:
        monsterGenerator.generate(m1=2, m2=2, m3=2)


def pause_input(key):
    if key == 'enter':    # press tab to toggle edit/play mode
        application.paused = not application.paused
        first_text.enabled = False


monsterGenerator.generate(m1=2, m2=2, m3=2)
pause_handler = Entity(ignore_paused=True, input=pause_input)

app.run()
