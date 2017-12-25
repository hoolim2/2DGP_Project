import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None
class BGMplayer:
    def __init__(self):
        self.soundloudness = 64
        self.BG_sound = load_music('resource\\music\\titleTheme.mp3')
        self.BG_sound.set_volume(self.soundloudness)

        self.BG_sound.repeat_play()

    def update(self):
        self.soundloudness -= 1
        self.BG_sound.set_volume(self.soundloudness)

class uiFadeout:
    def __init__(self):
        self.playanimation=0
        self.Yframes = 3
        self.play_frames = 0
        self.framepass = 0
        self.image = load_image('resource\\black_fadeout.png')

    def update(self,frame_time):
        self.playanimation+=frame_time
        if self.framepass>=7:
            self.play_frames = (self.play_frames + 1) % 5
            self.framepass=0
            if self.play_frames==0:
                self.Yframes -=1
        self.framepass += 1
        if self.playanimation>=1.5:
            self.Yframes = 3
            self.play_frames=0
            self.playdamage = 0

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames * 192, self.Yframes * 192, 192, 192, 0, -280, 1280, 1280)

def enter():
    global image,gameovertime,fadeout_fx,bgmplayer,font,changeScene,fadeoutTime,current_time
    image = load_image('resource\\title.png')
    bgmplayer = BGMplayer()
    gameovertime = 0
    changeScene = False
    fadeout_fx = uiFadeout()
    fadeoutTime=0.0
    current_time = 0.0
    pass


def exit():
    global  image,bgmplayer
    del(image)
    del(bgmplayer)
    pass


def handle_events():
    global changeScene
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type,event.key) ==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key) ==(SDL_KEYDOWN,SDLK_SPACE) :
                changeScene = True
    pass


def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    if frame_time<1:
        return frame_time
    else:
        return 0

def draw():
    global changeScene
    clear_canvas()
    image.draw(640,360)
    if changeScene == True:
        fadeout_fx.draw()

    update_canvas()
    delay(0.01)
    pass

def update():
    global fadeoutTime,bgmplayer
    frame_time = get_frame_time()
    if changeScene == True:
        fadeout_fx.update(frame_time)
        bgmplayer.update()
        fadeoutTime+=frame_time
        if fadeoutTime > 1.5:
            game_framework.change_state(main_state)

    pass


def pause():
    pass


def resume():
    pass






