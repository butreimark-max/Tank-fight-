import arcade
import Animation
import time

class Tanks_base(Animation.Animation):
    def __init__(self,image,hp,window):
        super().__init__(image,scale=0.12)
        self.window=window
        self.hp=hp

        self.row=0
        self.col=0
        self.timer=0
    def update(self):

        if self.hp<=0:

            self.kill()


class Tanks(Tanks_base):
    def __init__(self, window):
        super().__init__("pictures/Tank Blu_1.png",100,window )
        self.append_texture(arcade.load_texture("pictures/Tank Blu_1.png"))
        self.append_texture(arcade.load_texture("pictures/Tank Blu_2.png"))
        self.center_x = center_x
        self.center_y = center_y

        self.speed = speed

    def update(self):
        if self.hp <= 0:
            self.kill()