from tkinter import *
import random

GAME_WIDTH = 500
GAME_HEIGHT = 500
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#e2d64a"
FOOD_COLOR = "#FF0000"
BACKGROUND = '#000000'


class Snake:
    pass

def next_turn():
    pass
def change_direction(new_direction):
    pass
def check_collisions():
    pass
def game_over():
    pass

window = Tk()

window.title("Snake game")

window.resizable(False,False)

score = 0

direction = 'down'

label = Label(window, text = "Score:{}".format(score),font = ('consolas',40))
label.pack()

window.mainloop()