import random

import pygame
from pygame.surface import Surface



class Enemy:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("resource/enemy/play_babybear_run_0.png")
        self.rect = self.image.get_rect()
        self.x = self.screen_rect.width
        self.y = random.randrange(0, self.screen_rect.height - self.rect.height)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.x -= 3

        if self.x < -self.rect.width:
            self.x = self.screen_rect.width
            self.y = random.randrange(0, self.screen_rect.height - self.rect.height)
