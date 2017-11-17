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

right_key_down=False
left_key_down=False
up_key_down=False
isPlaying=False

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
    if(charNumX_one == -1):
        charNumX_one = charNumX_two
        charNumY_one = charNumY_two
        charNumX_two=-1
        charNumY_two=-1
    if (charNumX_two == -1):
        charNumX_two = charNumX_three
        charNumY_two = charNumY_three
        charNumX_three = -1
        charNumY_three = -1
    if (charNumX_three == -1):
        charNumX_three = charNumX_four
        charNumY_three = charNumY_four
        charNumX_four = -1
        charNumY_four = -1
    if (charNumX_four == -1):
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
        self.flyspd = 500*random.randrange(1, 5)
        self.delayTime = 0
        self.image = load_image('hero_sprite.png')

    def update(self,frame_time):
        global isPlaying, right_key_down, left_key_down, up_key_down,charNumX_one,charNumY_one
        if isPlaying==False:
            self.x += self.dir
            if self.x >= (640-charSize1/2)+5:
                self.dir = -10*frame_time
            elif self.x <= (640-charSize1/2)-5:
                self.dir = 10*frame_time
        elif isPlaying==True:
            self.delayTime+=frame_time
            if up_key_down == True and self.delayTime>0.4:
                self.y += 1500 * frame_time
            if self.delayTime > 0.7:
                if right_key_down == True:
                    self.x += 1500*frame_time
                    self.y += self.flyspd*frame_time
                    self.flyspd -= 5000*frame_time
                elif left_key_down == True:
                    self.x -= 1500*frame_time
                    self.y += self.flyspd * frame_time
                    self.flyspd -= 5000 * frame_time
            if self.x > 1280 or self.x < -charSize1 or self.y > 720:
                isPlaying = False
                right_key_down = False
                left_key_down = False
                up_key_down = False
                self.x, self.y = 640 - charSize1 / 2, 100
                self.flyspd=500*random.randrange(3, 6)
                self.delayTime=0
                charNumX_one = -1
                charNumY_one = -1

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

class slashEffect:

    def __init__(self):
        self.Yframes = 4
        self.play_frames = 0
        self.framepass=0
        self.image = load_image('fx_slash.png')

    def update(self):
        if isPlaying==True:
            if self.framepass>=2:
                self.play_frames = (self.play_frames + 1) % 5
                self.framepass=0
                if self.play_frames==0:
                    self.Yframes -=1
            self.framepass += 1
        if isPlaying==False:
            self.Yframes = 4

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames * 192, self.Yframes * 192, 192, 192, 390, -50, 500, 500)

class slashadEffect:

    def __init__(self):
        self.Yframes = 6
        self.play_frames = 0
        self.framepass=0
        self.image = load_image('fx_slashadvence.png')

    def update(self):
        if isPlaying==True:
            if self.framepass>=2:
                self.play_frames = (self.play_frames + 1) % 5
                self.framepass=0
                if self.play_frames==0:
                    self.Yframes -=1
            self.framepass += 1
        if isPlaying==False:
            self.Yframes = 6

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames * 192, self.Yframes * 192, 192, 192, 390, -50, 500, 500)

class magicEffect:

    def __init__(self):
        self.Yframes = 5
        self.play_frames = 0
        self.framepass=0
        self.image = load_image('fx_magic.png')

    def update(self):
        if isPlaying==True:
            if self.framepass>=2:
                self.play_frames = (self.play_frames + 1) % 5
                self.framepass=0
                if self.play_frames==0:
                    self.Yframes -=1
            self.framepass += 1
        if isPlaying==False:
            self.Yframes = 5

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames*192, self.Yframes*192,192,192,390,-50,500,500)

class drainEffect:

    def __init__(self):
        self.Yframes = 5
        self.play_frames = 0
        self.framepass = 0
        self.image = load_image('fx_darkness.png')

    def update(self):
        if isPlaying==True:
            if self.framepass>=2:
                self.play_frames = (self.play_frames + 1) % 5
                self.framepass=0
                if self.play_frames==0:
                    self.Yframes -=1
            self.framepass += 1
        if isPlaying==False:
            self.Yframes = 5

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames*192, self.Yframes*192,192,192,390,-50,500,500)

class healEffect:

    def __init__(self):
        self.Yframes = 4
        self.play_frames = 0
        self.framepass =0
        self.image = load_image('fx_heal.png')

    def update(self):
        if isPlaying==True:
            if self.framepass>=2:
                self.play_frames = (self.play_frames + 1) % 5
                self.framepass=0
                if self.play_frames==0:
                    self.Yframes -=1
            self.framepass += 1
        if isPlaying==False:
            self.Yframes = 4

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames*192, self.Yframes*192,192,192,390,-50,500,500)

class bloodEffect:

    def __init__(self):
        self.Yframes = 10
        self.play_frames = 0
        self.framepass =0
        self.image = load_image('fx_blood.png')

    def update(self):
        if isPlaying==True:
            if self.framepass>=2:
                self.play_frames = (self.play_frames + 1) % 5
                self.framepass=0
                if self.play_frames==0:
                    self.Yframes -=1
            self.framepass += 1
        if isPlaying==False:
            self.Yframes = 10

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames*192, self.Yframes*192,192,192,390,-50,500,500)

def enter():
    global background,line_one,line_two,line_three,line_four,line_five,slash_fx,magic_fx,heal_fx,drain_fx,slashad_fx,blood_fx
    createCharacter()
    line_one=lineOne()
    line_two = lineTwo()
    line_three = lineThree()
    line_four = lineFour()
    line_five = lineFive()
    slash_fx = slashEffect()
    slashad_fx = slashadEffect()
    magic_fx = magicEffect()
    heal_fx= healEffect()
    drain_fx= drainEffect()
    blood_fx = bloodEffect()

    background = Background()
    pass


def exit():
    global background,line_one,line_two,line_three,line_four,line_five,slash_fx,magic_fx,heal_fx,drain_fx,slashad_fx,blood_fx
    del(background)
    del(line_one)
    del(line_two)
    del(line_three)
    del(line_four)
    del (line_five)
    del (slash_fx)
    del (magic_fx)
    del (heal_fx)
    del(drain_fx)
    del (blood_fx)
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
    global right_key_down,left_key_down,up_key_down,isPlaying
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            interrogation()
        if isPlaying == False:
            if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
                right_key_down = True
                isPlaying=True
            elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
                left_key_down = True
                isPlaying = True
            elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
                up_key_down=True
                isPlaying = True
    pass

def update():
    createCharacter()
    frame_time=get_frame_time()
    line_one.update(frame_time)
    line_two.update(frame_time)
    line_three.update(frame_time)
    line_four.update(frame_time)
    line_five.update(frame_time)
    slash_fx.update()
    slashad_fx.update()
    magic_fx.update()
    heal_fx.update()
    drain_fx.update()
    blood_fx.update()

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
    #-------------------
    if left_key_down == True:
        if isPlaying == True:
            blood_fx.draw()
            slash_fx.draw()
            slashad_fx.draw()

    if right_key_down == True:
        if isPlaying==True:
            blood_fx.draw()
            drain_fx.draw()
            magic_fx.draw()


    if up_key_down == True:
        if isPlaying == True:
            heal_fx.draw()
    #-----------------
    update_canvas()

    delay(0.01)
    pass

def changeLine():
    pass

def interrogation():
    pass


