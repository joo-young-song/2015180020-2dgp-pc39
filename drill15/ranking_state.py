import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import boy

import world_build_state

name = "MainState"


def collide(a, b):
    pass

ranking_list = None

def enter():
    global ranking_list
    with open('ranking_data.json', 'r') as f:
        ranking_list = json.load(f)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)

def update():
    pass



def draw():
    global ran
    clear_canvas()
    font = load_font('ENCR10B.TTF', 20)
    for i in range(len(ranking_list)):
        font.draw( 50 , i * 50, '(Time: %3.2f)' % (ranking_list[i]), (240, 0, 0))

    update_canvas()






