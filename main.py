import arcade
from Constants import *
from Tanks import Tanks, Bullet
import Base

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height,title)
        self.bg_picture = arcade.load_texture("pictures/bg/bg_new.png" , flipped_horizontally=True)
        self.tank=Tanks(self,100,100,5)
        self.left_press=False
        self.right_press=False
        self.up_press=False
        self.down_press=False
        self.projectiles=arcade.SpriteList()
        self.base_1=Base.Base(image="pictures/Base.png")
        self.base_2=Base.Base(image="pictures/Base.png")


        self.setup()
    def setup(self):
        self.base_1.set_position(100,350)
        self.base_2.set_position(SCREEN_WIDTH-100,350 )
        self.base_2.color = (255, 0, 0)
        self.base_1.angle = 90
        self.base_2.angle = -90


    def on_draw(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg_picture)
        self.tank.draw()
        self.projectiles.draw()
        self.base_2.draw()
        self.base_1.draw()
    def update(self, delta_time):
        self.tank.update()
        self.projectiles.update()
        if self.tank.moveing:
            self.tank.update_animation(delta_time)
    def on_key_press(self, key, modifiers):
        if key == arcade.key.A and not self.right_press:
            self.tank.change_angle=2.5
            self.tank.moveing=True
            self.left_press=True
            self.right_press=False
        if key == arcade.key.D and not self.left_press:
            self.tank.change_angle=-2.5
            self.tank.moveing = True
            self.left_press = False
            self.right_press = True
        if key == arcade.key.W and not self.down_press :
            self.tank.change_y = 4
            self.tank.change_x=4
            self.tank.moveing = True
            self.up_press=True
            self.down_press=False
        if key == arcade.key.S and not self.up_press:
            self.tank.change_y = -4
            self.tank.change_x = -4
            self.tank.moveing = True
            self.down_press=True
            self.up_press=False

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.A and not self.right_press:
            self.tank.change_angle = 0
            self.tank.moveing = False
            self.left_press = False
            self.right_press = False
        if key == arcade.key.D and not self.left_press:
            self.tank.change_angle = 0
            self.tank.moveing = False
            self.left_press = False
            self.right_press = False
        if key == arcade.key.W and not self.down_press:
            self.tank.change_y = 0
            self.tank.change_x = 0
            self.tank.moveing = False
            self.down_press = False
            self.up_press = False
        if key == arcade.key.S and not self.up_press:
            self.tank.change_y = 0
            self.tank.change_x = 0
            self.tank.moveing = False
            self.down_press = False
            self.up_press = False
    def on_mouse_press(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            shell=Bullet("pictures/Tank Blu_1.png",self.tank)
            self.projectiles.append(shell)


    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        pass
    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


window=MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
arcade.run()