import pygame
from pygame import Surface


class Boss:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.screen_size = self.screen.get_size()
        self.images = tuple(pygame.image.load(f"./resource/boss_run/play_mombear_run_{i}.png") for i in range(7))

        self.x = 1000
        self.y = (self.screen_size[1] // 2) - (self.images[0].get_size()[1] // 2)

        self.run_count = 0
        self.image_per_frame = 30

        self.hp_image = pygame.image.load("./resource/hp.png")
        self.hp_bar_image = pygame.image.load("./resource/hp_bar.png")

    def draw(self):
        self.screen.blit(self.images[self.run_count // self.image_per_frame], (self.x, self.y))
        self.screen.blit(self.hp_bar_image, (self.x + 30, self.y), (0, 0, 55, 20))
        self.screen.blit(self.hp_image, (self.x + 30, self.y), (0, 0, 55, 20))

    def animation(self):
        self.run_count += 1
        self.run_count %= len(self.images) * self.image_per_frame
