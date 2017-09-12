# --------------------------------
#       ALIENS SAMPLE
# --------------------------------

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Draw the ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()  # NOTE: THIS IS INTERESTING CONCEPT

    # Start main loop for game
    while True:

        # Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in bullets.copy():  # Loop over copy instead of actual
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
