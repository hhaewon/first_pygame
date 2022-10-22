import pygame
from pygame.surface import Surface

from boss import Boss
from enemy import Enemy

class Missile:
    def __init__(self, screen: Surface, boss: Boss, enemies: list[Enemy]):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.boss = boss
        self.enemies = enemies

        self.image1 = pygame.image.load("resource/bullet.png")
        self.image2 = pygame.image.load("resource/bullet2.png")

        self.speed = 10
        self.damage = 5
        self.accumulated_damage = 0

        self.positions1: list[tuple[int]] = []
        self.positions2: list[tuple[int]] = []

        self.is_shot = False

    def draw(self):
        x: int
        y: int
        for (x, y) in self.positions1:
            self.screen.blit(self.image1, (x, y))
        for x, y in self.positions2:
            self.screen.blit(self.image2, (x, y))


    def update(self):
        x: int
        y: int
        for index, (x, y) in enumerate(self.positions1):
            new_x = x + self.speed
            if new_x < self.screen_rect.width:
                self.positions1[index] = (new_x, y)
            else:
                del self.positions1[index]
                continue

            if (self.boss.x <= x <= self.boss.x + self.boss.rect.width
                and self.boss.y <= y <= self.boss.y + self.boss.rect.height):

                self.is_shot = True
                self.accumulated_damage += self.damage
                del self.positions1[index]
                continue

            for index_enemy, enemy in enumerate(self.enemies):
                if (enemy.x <= x <= enemy.x + enemy.rect.width
                    and enemy.y <= y <= enemy.y + enemy.rect.height):

                    del self.positions1[index]
                    del self.enemies[index_enemy]
                    self.enemies.append(Enemy(screen=self.screen))
                    break

        for index, (x, y) in enumerate(self.positions2):
            new_y = y - self.speed
            if new_y < self.screen_rect.height:
                self.positions2[index] = (x, new_y)
            else:
                del self.positions2[index]
                continue

            if (self.boss.x <= x <= self.boss.x + self.boss.rect.width
                    and self.boss.y <= y <= self.boss.y + self.boss.rect.height):

                self.is_shot = True
                self.accumulated_damage += self.damage
                del self.positions2[index]
                continue

            for index_enemy, enemy in enumerate(self.enemies):
                if (enemy.x <= x <= enemy.x + enemy.rect.width
                    and enemy.y <= y <= enemy.y + enemy.rect.height):

                    del self.positions2[index]
                    del self.enemies[index_enemy]
                    self.enemies.append(Enemy(screen=self.screen))
                    break

        if self.is_shot:
            self.boss.hp -= self.accumulated_damage
            if self.boss.hp <= 0:
                self.boss.is_dead = True
            self.is_shot = False
            self.accumulated_damage = 0



