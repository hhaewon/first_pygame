import random

import pygame
from pygame import Surface


class Enemy:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.image = pygame.image.load("resource/enemy/play_babybear_run_0.png")
        self.size = self.image.get_size()
        self.x = random.randrange(0, self.screen.get_size()[0] - self.image.get_size()[0])
        self.y = random.randrange(0, self.screen.get_size()[1] - self.image.get_size()[1])

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.x -= 3

        if self.x < -self.size[0]:
            self.x = self.screen.get_size()[0]
            self.y = random.randrange(0, self.screen.get_size()[1] - self.image.get_size()[1])
