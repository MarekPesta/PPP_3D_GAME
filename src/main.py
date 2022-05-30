from config import *

app = Ursina()

random.seed(0)

#Entity.default_shader = lit_with_shadows_shader

ground = Entity(model='plane', collider='box', scale=64, texture='floor', texture_scale=(16, 16))
wall1 = Entity(model='quad', collider='box', x=0, y=32, z=32, scale=64, texture='wall', texture_scale=(8, 8))
wall2 = Entity(model='quad', collider='box', x=32, y=32, z=0, rotation_y=90, scale=64, texture='wall', texture_scale=(8, 8))
wall3 = Entity(model='quad', collider='box', x=0, y=32, z=-32, rotation_y=180, scale=64, texture='wall', texture_scale=(8, 8))
wall4 = Entity(model='quad', collider='box', x=-32, y=32, z=0, rotation_y=270, scale=64, texture='wall', texture_scale=(8, 8))
top = Entity(model='quad', collider='box', x=0, y=64, z=0, rotation_x=-90, scale=64, texture='top', texture_scale=(4, 4))

player = FirstPersonController(speed=8, x=-10, z=-10)

class CubeSolid(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(parent=scene,
                         position=position,
                         model='cube',
                         origin_y=.5,
                         texture='solid_cube',
                         color=color.color(0, 0, random.uniform(.9, 1.0)),
                         highlight_color=color.lime)

class CubeMod(Button):
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

def input(key):
    if key == "escape":
        # Escape Key Pressed... Quit
        quit()

    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            CubeMod(position=hit_info.entity.position + hit_info.normal)

def update():
    if held_keys['left shift']:
        player.speed = 20
    else:
        player.speed = 8


hammer_handle = Entity(model='cube', parent=camera, position=(.5,-.7,1), scale=(.1,1,.1), origin_z=-.5, texture='hammer_handle', on_cooldown=False)
hammer_top = Entity(model='cube', parent=camera, position=(.5,-.1,0.9), scale=(.3,.3,.5), origin_z=-.5, texture='hammer_top', on_cooldown=False)
# hammer = Entity(model='cube', parent=camera, rotation_x=0, position=(.5,-.25,.25), scale=(.3,.2,1), origin_z=-.5, color=color.red, on_cooldown=False)




#gun = Entity(model='cube', parent=camera, position=(.5,-.25,.25), scale=(.3,.2,1), origin_z=-.5, color=color.red, on_cooldown=False)
#gun.muzzle_flash = Entity(parent=gun, z=1, world_scale=.5, model='quad', color=color.yellow, enabled=False)


app.run()
