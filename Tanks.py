import arcade

# from arcade.examples.perf_test.stress_test_collision_arcade import SCREEN_WIDTH
from Constants import *
from pyglet.libs.win32.constants import SPACEPARITY

import Animation
import time
import math
class Tanks_base(Animation.Animation):
    def __init__(self,image,hp,window):
        super().__init__(image,scale=2)
        self.window=window
        self.hp=hp
        self.active=True
        self.moveing=False
        self.angle=0

        self.timer=0
    def update(self):

        if self.active:
            self.angle+=self.change_angle
            self.part_x=math.cos(math.radians(self.angle))
            self.part_y=math.sin(math.radians(self.angle))
            self.center_x+=self.change_x*self.part_x
            self.center_y+=self.change_y*self.part_y

        if self.hp<=0:

            self.active=False


class Tanks(Tanks_base):
    def __init__(self, window,center_x,center_y,speed):
        super().__init__("pictures/Tank Blu_1.png",100,window )
        self.append_texture(arcade.load_texture("pictures/Tank Blu_1.png"))
        self.append_texture(arcade.load_texture("pictures/Tank Blu_2.png"))
        self.center_x = center_x
        self.center_y = center_y

        self.speed = speed
class Bullet(arcade.Sprite):
    def __init__(self,image,tank):
        super().__init__(image,scale=0.5)
        self.change_x=12*tank.part_x
        self.change_y=12*tank.part_y

        self.center_x=tank.center_x
        self.center_y=tank.center_y
        self.angle=tank.angle


    def update(self):
        self.center_x+=self.change_x
        self.center_y+=self.change_y
        if self.left > SCREEN_WIDTH or self.right < 0 or self.bottom> SCREEN_HEIGHT or self.top < 0:
            self.kill()
