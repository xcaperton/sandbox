# Build rocket
import pygame
from random import randint


class Rocket():
    """This is a rocket class"""

    def __init__(self, r_settings, screen):
        self.r_settings = r_settings
        self.screen = screen

        self.image = pygame.image.load("images/rocket.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship in the center bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw the ship"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the Rocket location"""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.r_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.r_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.r_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.r_settings.ship_speed_factor

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def teleport(self):
        self.center_x = randint(0, self.r_settings.screen_width)
        self.center_y = randint(0, self.r_settings.screen_height)

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y
