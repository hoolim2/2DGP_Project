import game_framework
import title_state
import main_state
import start_state

from pico2d import *


name = "GameOverState"
image = None


def enter():
    global image
    image = load_image('resource\\gameover.png')
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
    update_canvas()
    pass

def update():
    pass


def pause():
    pass


def resume():
    pass


