import arcade
from Constants import *


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height,title)
        self.bg_picture = arcade.load_texture("pictures/bg/bg.png")


        self.setup()
    def setup(self):
        pass
    def on_draw(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg_picture)

    def update(self, delta_time):
        pass
    def on_mouse_press(self, x, y, button, key_modifiers):
        pass
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        pass
    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


window=MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TILE)
arcade.run()