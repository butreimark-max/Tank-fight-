from Constants import *
import arcade
class Base(arcade.Sprite):
    def __init__(self, image):
        super().__init__(image, 0.2)
        self.hp=100
    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x, self.center_y+200,180, 15,(0,255,0),3)
        width=1.8*self.hp
        indent=((100-width)*1.8)/2
        x=self.center_x+indent
        arcade.draw_rectangle_filled(x,self.center_y+200,width,13,(255,255,0))