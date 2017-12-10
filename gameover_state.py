import game_framework
import title_state
import main_state
import start_state

from pico2d import *


name = "GameOverState"
image = None
class BGMplayer:
    def __init__(self):
        self.BG_sound = load_music('resource\\music\\gameoverTheme.mp3')
        self.BG_sound.set_volume(64)

        self.BG_sound.repeat_play()



def enter():
    global image,bgmplayer,font
    image = load_image('resource\\gameover.png')

    font = None

    if font == None:
        font = load_font('resource\\moris9.TTF', 40)

    bgmplayer=BGMplayer()
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
                game_framework.change_state(title_state)
    pass


def draw():
    clear_canvas()
    image.draw(640,360)
    drawScore = main_state.totalScore
    font.draw(550, 250, 'Score: %d' % (int(drawScore)), (255, 255, 255))
    update_canvas()
    pass

def update():
    pass


def pause():
    pass


def resume():
    pass


