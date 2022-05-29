# Libs
from rich import print
from rich.traceback import install
install(show_locals=False)

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
#from ursina.shaders import lit_with_shadows_shader