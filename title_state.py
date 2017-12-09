import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None
class BGMplayer:
    def __init__(self):
        self.BG_sound = load_music('resource\\music\\titleTheme.mp3')
        self.BG_sound.set_volume(64)

        self.BG_sound.repeat_play()


def enter():
    global image,gameovertime,fadeout_fx,bgmplayer
    image = load_image('resource\\title.png')
    bgmplayer = BGMplayer()
    gameovertime = 0
    pass


def exit():
    global  image
    del(image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type,event.key) ==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key) ==(SDL_KEYDOWN,SDLK_SPACE) :
                game_framework.change_state(main_state)
    pass


def draw():
    clear_canvas()
    image.draw(640,360)
    update_canvas()
    pass

def update():
    pass


def pause():
    pass


def resume():
    pass






