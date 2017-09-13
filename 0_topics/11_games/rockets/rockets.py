# Rockets.py

import sys
import pygame
from settings import Settings
from rocket import Rocket
import game_functions as gf


def run_game():
    # Intialize the game
    pygame.init()
    r_settings = Settings()
    screen = pygame.display.set_mode(
        (r_settings.screen_width, r_settings.screen_height))
    pygame.display.set_caption("Rockets")

    # Will need to draw ship
    rocket = Rocket(r_settings, screen)

    # Main game loop
    while True:

        # Watch for keyboard events
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(r_settings, screen, rocket)


run_game()
