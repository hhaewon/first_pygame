import typing

import pygame
from pygame.surface import Surface

class MoveFlag(typing.TypedDict):
    right: bool
    left: bool
    up: bool
    down: bool


class Player:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.screen_size = self.screen.get_rect()

        self.standing_images = tuple(
            pygame.image.load(f"./resource/standing/play_atti_standing_{i}.png") for i in range(4)
        )
        self.run_right_images = tuple(
            pygame.image.load(f"./resource/run_right/play_atti_run_{i}.png") for i in range(4)
        )
        self.attack_images = tuple(
            pygame.image.load(f"./resource/attack/play_atti_attack0_{i}.png") for i in range(9)
        )

        self.size = self.standing_images[0].get_rect()
        self.x = 250
        self.y = 300

        self.move_flag: MoveFlag = {
            'right': False,
            'left': False,
            'up': False,
            'down': False,
        }
        self.is_attack = False

        self.standing_count = 0
        self.run_right_count = 0
        self.attack_count = 0
        self.image_per_frame = 30

    def draw(self):
        if self.is_attack:
            self.screen.blit(self.attack_images[self.attack_count // self.image_per_frame], (self.x, self.y))
        elif self.move_flag['right']:
            self.screen.blit(self.run_right_images[self.run_right_count // self.image_per_frame], (self.x, self.y))

        else:
            self.screen.blit(self.standing_images[self.standing_count // self.image_per_frame], (self.x, self.y))

    def update(self):
        if self.move_flag['right'] and self.x < self.screen_size.width - self.size.width:
            self.x += 2
        if self.move_flag['left'] and self.x > 0:
            self.x -= 2
        if self.move_flag['up'] and self.y > 0:
            self.y -= 2
        if self.move_flag['down'] and self.y < self.screen_size.height - self.size.height:
            self.y += 2

    def animation(self):
        self.standing_count += 1
        self.run_right_count += 1
        self.attack_count += 1

        self.standing_count %= len(self.standing_images) * self.image_per_frame
        self.run_right_count %= len(self.run_right_images) * self.image_per_frame
        self.attack_count %= len(self.attack_images) * self.image_per_frame
