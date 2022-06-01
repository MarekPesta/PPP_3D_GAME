from config import *
from miscellaneous import CubeModifiable


class Weapon:

    def __init__(self):
        self.weapon_elements = []
        self.enabled = False
        self.hud = False
        self.single_shot = None

        self.ammo = None
        self.magazine_ammo = None
        self.damage = None

    def enable(self):
        for elemnt in self.weapon_elements:
            elemnt.enabled = True
        self.enabled = True

    def disable(self):
        for elemnt in self.weapon_elements:
            elemnt.enabled = False
        self.enabled = False

    def single_action(self):
        if self.single_shot is True:
            self._single_action()

    def multi_action(self):
        if self.single_shot is False:
            self._multi_action()

    def _single_action(self):
        raise NotImplementedError(f'{self}: attempt to use `single_action` method without `_single_action` implementation.')

    def _multi_action(self):
        raise NotImplementedError(f'{self}: attempt to use `multi_action` method without `_multi_action` implementation.')


class Nufin(Weapon):

    def __init__(self):
        super().__init__()
        self.single_shot = True

    def _single_action(self):
        pass


class Hammer(Weapon):

    def __init__(self):
        super().__init__()
        hammer_handle = Entity(model='cube', parent=camera, position=(.5, -.7, 1), scale=(.1, 1, .1), origin_z=-.5, texture='hammer_handle', on_cooldown=False)
        hammer_top = Entity(model='cube', parent=camera, position=(.5, -.1, 0.9), scale=(.3, .3, .5), origin_z=-.5, texture='hammer_top', on_cooldown=False)

        self.weapon_elements.append(hammer_handle)
        self.weapon_elements.append(hammer_top)
        self.single_shot = True
        self.disable()

    def _single_action(self):
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            CubeModifiable(position=hit_info.entity.position + hit_info.normal)


class Rifle(Weapon):

    def __init__(self):
        super().__init__()
        self.gun = Entity(model='guns/m4a1.obj', parent=camera, position=(.9,-1,2.5), scale=0.5, rotation_y=180, origin_z=-.75, texture='guns/m4a1.jpg', on_cooldown=False, double_sided=True)
        self.gun.muzzle_flash = Entity(parent=camera, position=(0.95,-.4,4.5), scale=0.3, model='sphere', color=color.yellow, enabled=False)

        self.single_shot = False

        self.weapon_elements.append(self.gun)
        self.disable()

    def _multi_action(self):

        gun = self.gun

        if not gun.on_cooldown:
            # print('shoot')
            gun.on_cooldown = True
            gun.muzzle_flash.enabled = True
            from ursina.prefabs.ursfx import ursfx
            ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)], volume=0.5, wave='noise', pitch=random.uniform(-13,-12), pitch_change=-12, speed=3.0)
            invoke(gun.muzzle_flash.disable, delay=.05)
            invoke(setattr, gun, 'on_cooldown', False, delay=.15)
            if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp'):
                mouse.hovered_entity.hp -= 10
                mouse.hovered_entity.blink(color.red)


# self.gun = Entity(model='my_obj/Gun.obj', parent=camera, position=(.5,-.25,.5), scale=1, origin_z=-.5, texture='my_obj/Gun', on_cooldown=False)
#self.gun = Entity(model='guns/m4a1.obj', parent=camera, position=(.5,-.2,1), scale=1, origin_z=-.5, texture='guns/m4a1.jpg', on_cooldown=False, double_sided=True)
#self.gun = Entity(model='guns/railgun.obj', parent=camera, position=(.5,-.2,10), scale=10, origin_z=-.5, texture='guns/railgun.jpg', on_cooldown=False, double_sided=True)
