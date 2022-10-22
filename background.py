import pygame


class Background:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("resource/game_background.png")
        self.image2 = pygame.image.load("resource/game_background.png")
        self.x1 = 0
        self.y1 = 0
        self.x2 = self.screen_rect[0]
        self.y2 = 0

    def draw(self):
        self.screen.blit(self.image, (self.x1, self.y1))
        self.screen.blit(self.image2, (self.x2, self.y2))

    def update(self):
        self.x1 -= 2
        self.x2 -= 2

        if self.x1 <= -self.screen_rect[0]:
            self.x1 = self.screen_rect[0]
        if self.x2 <= -self.screen_rect[0]:
            self.x2 = self.screen_rect[0]
