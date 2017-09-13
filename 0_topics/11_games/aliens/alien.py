# Alien Class

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single in the fleet"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
