from config import *


class MyWorld:
    def __init__(self):

        random.seed(0)

        self.ground = Entity(model='plane', collider='box', scale=64, texture='floor', texture_scale=(16, 16))
        self.wall1 = Entity(model='quad', collider='box', x=0, y=32, z=32, scale=64, texture='wall', texture_scale=(8, 8))
        self.wall2 = Entity(model='quad', collider='box', x=32, y=32, z=0, rotation_y=90, scale=64, texture='wall', texture_scale=(8, 8))
        self.wall3 = Entity(model='quad', collider='box', x=0, y=32, z=-32, rotation_y=180, scale=64, texture='wall', texture_scale=(8, 8))
        self.wall4 = Entity(model='quad', collider='box', x=-32, y=32, z=0, rotation_y=270, scale=64, texture='wall', texture_scale=(8, 8))
        self.top = Entity(model='quad', collider='box', x=0, y=64, z=0, rotation_x=-90, scale=64, texture='top', texture_scale=(4, 4))

        for z in range(2):
            for x in range(2):
                CubeSolid(position=(x, 1, z))

        for z in range(2):
            for x in range(2):
                CubeSolid(position=(x+31, 1, z+31))

        for z in range(2):
            for x in range(2):
                CubeSolid(position=(x-32, 1, z-32))

        for z in range(2):
            for x in range(2):
                CubeSolid(position=(x-32, 1, z+31))

        for z in range(2):
            for x in range(2):
                CubeSolid(position=(x+31, 1, z-32))

        shootables_parent = Entity()
        mouse.traverse_target = shootables_parent


class CubeSolid(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(parent=scene,
                         position=position,
                         model='cube',
                         origin_y=.5,
                         texture='solid_cube',
                         color=color.color(0, 0, random.uniform(.9, 1.0)),
                         highlight_color=color.lime)


class CubeModifiable(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(parent=scene,
                         position=position,
                         model='cube',
                         origin_y=.5,
                         texture='mod_cube',
                         color=color.color(0, 0, random.uniform(.9, 1.0)),
                         highlight_color=color.lime)

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                hit_info = raycast(camera.world_position, camera.forward, distance=5)
                if hit_info.hit:
                    destroy(self)
