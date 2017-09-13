# Game Functions

import sys
import pygame


def check_events(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def check_keydown_events(event, rocket):
    """Check for keyboard presses"""
    if event.key == pygame.K_LEFT:
        rocket.moving_left = True
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    if event.key == pygame.K_DOWN:
        rocket.moving_down = True
    if event.key == pygame.K_UP:
        rocket.moving_up = True
    if event.key == pygame.K_t:
        rocket.teleport()


def check_keyup_events(event, rocket):
    """Check for keyboard presses"""
    if event.key == pygame.K_LEFT:
        rocket.moving_left = False
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    if event.key == pygame.K_DOWN:
        rocket.moving_down = False
    if event.key == pygame.K_UP:
        rocket.moving_up = False


def update_screen(r_settings, screen, rocket):
    screen.fill(r_settings.bg_color)
    rocket.blitme()

    pygame.display.flip()
