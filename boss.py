import random
import math
import typing

import pygame
from pygame.surface import Surface

class Boss:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.images = tuple(pygame.image.load(f"./resource/boss_run/play_mombear_run_{i}.png") for i in range(7))
        self.hp_image = pygame.image.load("./resource/hp.png")
        self.full_hp_image = pygame.image.load("./resource/hp_bar.png")

        self.rect = self.images[0].get_rect()
        self.full_hp = 55
        self.hp = 55
        self.x = random.randrange(0, self.screen_rect.width - self.rect.width)
        self.y = random.randrange(0, self.screen_rect.height - self.rect.height)
        self.speed = 1.5
        self.x_sign = 1
        self.y_sign = 1
        self.angle = 220

        self.run_count = 0
        self.image_per_frame = 30

        self.is_dead = False


    def draw(self):
        if not self.is_dead:
            self.screen.blit(self.images[self.run_count // self.image_per_frame], (self.x, self.y))
            self.screen.blit(self.full_hp_image, (self.x + 30, self.y), (0, 0, self.full_hp, 20))
            self.screen.blit(self.hp_image, (self.x + 30, self.y), (0, 0, self.hp, 20))

    def update(self):
        distance_x = math.sin(math.radians(self.angle)) * self.speed * self.x_sign
        distance_y = math.cos(math.radians(self.angle)) * self.speed * self.y_sign
        self.x += distance_x
        self.y += distance_y

        if (self.x < 0) or (self.x >= self.screen_rect.width - self.rect.width):
            self.x_sign *= -1

        if (self.y < 0) or (self.y >= self.screen_rect.height - self.rect.height):
            self.y_sign *= -1


    def animation(self):
        self.run_count += 1
        self.run_count %= len(self.images) * self.image_per_frame


