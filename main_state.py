import random
import json
import os

from pico2d import *

import game_framework
import title_state


name = "MainState"

pause = None
line_one = None
line_two = None
line_three = None
line_four=None
line_five=None
background = None
font = None

#====================
charNumX_one, charNumX_two, charNumX_three, charNumX_four=-1,-1,-1,-1
charNumY_one, charNumY_two, charNumY_three, charNumY_four=-1,-1,-1,-1
charNumX_five= random.randrange(0, 11)
charNumY_five= random.randrange(0, 7)
#====================

charsize=53

charSize1=220
charSize2=160
charSize3=130
charSize4=105
charSize5=95
charSize6=80

def createCharacter():
    global charNumX_one,charNumX_two,charNumX_three,charNumX_four,charNumX_five
    global charNumY_one,charNumY_two,charNumY_three,charNumY_four,charNumY_five
    if(charNumX_one == -1.):
        charNumX_one = charNumX_two
        charNumY_one = charNumY_two
        charNumX_two=-1
        charNumY_two=-1
    if (charNumX_two == -1.):
        charNumX_two = charNumX_three
        charNumY_two = charNumY_three
        charNumX_three = -1
        charNumY_three = -1
    if (charNumX_three == -1.):
        charNumX_three = charNumX_four
        charNumY_three = charNumY_four
        charNumX_four = -1
        charNumY_four = -1
    if (charNumX_four == -1.):
        charNumX_four = charNumX_five
        charNumY_four = charNumY_five
        charNumX_five = -1
        charNumY_five = -1
    if (charNumX_five == -1):
        charNumX_five = random.randrange(0, 11)
        charNumY_five = random.randrange(0, 7)


class Background:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(640, 360)


class lineOne:
    def __init__(self):
        self.x, self.y = 640-charSize1/2,100
        self.dir=1
        self.image = load_image('hero_sprite.png')

    def update(self,frame_time):
        self.x += self.dir
        if self.x >= (640-charSize1/2)+5:
            self.dir = -10*frame_time
        elif self.x <= (640-charSize1/2)-5:
            self.dir = 10*frame_time

    def draw(self):
        self.image.clip_draw_to_origin(charNumX_one*charsize,charNumY_one*charsize,charsize,charsize,self.x,self.y,charSize1,charSize1)
        self.image.clip_draw

class lineTwo:
    def __init__(self):
        self.x, self.y = 640-charSize2/2,200
        self.dir=-1
        self.image = load_image('hero_sprite.png')

    def update(self,frame_time):
        self.x += self.dir
        if self.x >= (640-charSize2/2)+3:
            self.dir = -5*frame_time
        elif self.x <= (640-charSize2/2)-3:
            self.dir = 5*frame_time

    def draw(self):
        self.image.clip_draw_to_origin(charNumX_two*charsize,charNumY_two*charsize,charsize,charsize,self.x,self.y,charSize2,charSize2)

class lineThree:
    def __init__(self):

        self.x = 640-charSize3/2
        self.y =250
        self.dir=-1
        self.image = load_image('hero_sprite.png')

    def update(self,frame_time):
        self.x += self.dir
        if self.x >= (640-charSize3/2)+1:
            self.dir = -2*frame_time
        elif self.x <= (640-charSize3/2)-1:
            self.dir = 2*frame_time
        pass

    def draw(self):
        self.image.clip_draw_to_origin(charNumX_three*charsize,charNumY_three*charsize,charsize,charsize,self.x,self.y,charSize3,charSize3)

class lineFour:
    def __init__(self):
        self.x = 640-charSize4/2
        self.y =300
        self.dir=1
        self.image = load_image('hero_sprite.png')

    def update(self,frame_time):
        self.x += self.dir
        if self.x >= (640-charSize4/2)+1:
            self.dir = -2*frame_time
        elif self.x <= (640-charSize4/2)-1:
            self.dir = 2*frame_time
        pass

    def draw(self):
        self.image.clip_draw_to_origin(charNumX_four*charsize,charNumY_four*charsize,charsize,charsize,self.x,self.y,charSize4,charSize4)


class lineFive:
    global changeSign
    def __init__(self):
        self.x = 640-charSize5/2
        self.y =330
        self.dir=-1
        self.image = load_image('hero_sprite.png')

    def update(self,frame_time):
        self.x += self.dir
        if self.x >= (640-charSize5/2)+1:
            self.dir = -1*frame_time
        elif self.x <= (640-charSize5/2)-1:
            self.dir = 1*frame_time

    def draw(self):
        self.image.clip_draw_to_origin(charNumX_five*charsize,charNumY_five*charsize,charsize,charsize,self.x,self.y,charSize5,charSize5)

def enter():
    global background,line_one,line_two,line_three,line_four,line_five
    createCharacter()
    line_one=lineOne()
    line_two = lineTwo()
    line_three = lineThree()
    line_four = lineFour()
    line_five = lineFive()

    background = Background()
    pass


def exit():
    global background,line_one,line_two,line_three,line_four,line_five
    del(background)
    del(line_one)
    del(line_two)
    del(line_three)
    del(line_four)
    del (line_five)
    del(pause)
    pass


def pause():
    pass


def resume():
    pass


current_time = 0.0

def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def handle_events():
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            changeLine()
    pass

# team FACTORY
def update():
    createCharacter()
    frame_time=get_frame_time()
    line_one.update(frame_time)
    line_two.update(frame_time)
    line_three.update(frame_time)
    line_four.update(frame_time)
    line_five.update(frame_time)

    pass


def draw():
    clear_canvas()
    background.draw()
    #------------------
    line_five.draw()
    line_four.draw()
    line_three.draw()
    line_two.draw()
    line_one.draw()
    #-----------------
    update_canvas()
    pass

def changeLine():
    global charNumX_one,charNumY_one
    charNumX_one=-1.
    charNumY_one = -1.
    pass