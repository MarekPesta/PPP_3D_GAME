from config import *
from ursina.prefabs.health_bar import HealthBar
from monster_slayer import MonsterSlayer
import random


shootables_parent = Entity()
mouse.traverse_target = shootables_parent


class Enemy(Entity):
    def __init__(self, player: MonsterSlayer, obj, skin, scale, origin_y=-.5, hp=100, **kwargs):

        super().__init__(parent=shootables_parent, model=obj, scale=scale, origin_y=origin_y, texture=skin, collider='box', **kwargs)
        self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red, world_scale=(1.5,.1,.1))
        self.max_hp = hp
        self.hp = self.max_hp
        self.player = player
        self.speed = 5
        self.damage = 10

    def update(self):
        dist = distance_xz(self.player.controller.position, self.position)
        # if dist > 40:
        #     return

        self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)


        self.look_at_2d(self.player.controller.position, 'y')
        hit_info = raycast(self.world_position + Vec3(0,1,0), self.forward, 30, ignore=(self,))
        if hit_info.entity == self.player.controller:
            if dist > 2:
                self.position += self.forward * time.dt * self.speed

        if dist < 2:
            self.player.hp -= self.damage

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        if value <= 0:
            destroy(self)
            return

        self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
        self.health_bar.alpha = 1


class Unicorn(Enemy):

    def __init__(self, player: MonsterSlayer, **kwargs):

        self.obj ='cube'
        self.skin = 'unicorn'
        super().__init__(player=player, obj=self.obj, skin=self.skin, scale=10, hp=100, **kwargs)

        self.max_hp = 100
        self.speed = 5


class Monster1(Enemy):

    def __init__(self, player: MonsterSlayer, **kwargs):

        obj ='monsters/monster1'
        skin = 'monsters/monster1'
        super().__init__(player=player, obj=obj, skin=skin, scale=1, origin_y=-2, hp=50, **kwargs)

        self.max_hp = 50
        self.speed = 10


class Monster2(Enemy):

    def __init__(self, player: MonsterSlayer, **kwargs):

        self.obj ='monsters/monster2'
        self.skin = 'monsters/monster2.jpg'
        super().__init__(player=player, obj=self.obj, skin=self.skin, scale=0.02, origin_y=0, hp=120, **kwargs)

        self.max_hp = 120
        self.speed = (1/0.02)*3


class Monster3(Enemy):

    def __init__(self, player: MonsterSlayer, **kwargs):

        self.obj ='monsters/monster3'
        self.skin = 'monsters/monster3'
        super().__init__(player=player, obj=self.obj, skin=self.skin, scale=1, origin_y=0, hp=500, **kwargs)

        self.max_hp = 500
        self.speed = 2


class MonsterGenerator():

    def __init__(self, player: MonsterSlayer):
        self.enemies = []
        self.player = player

    def generate(self, m1, m2, m3):
        self.enemies.append([Monster1(player=self.player, z=random.randint(-25, 25), x=random.randint(-25, 25)) for x in range(m1)])
        self.enemies.append([Monster2(player=self.player, z=random.randint(-25, 25), x=random.randint(-25, 25)) for x in range(m2)])
        self.enemies.append([Monster3(player=self.player, z=random.randint(-25, 25), x=random.randint(-25, 25)) for x in range(m3)])
