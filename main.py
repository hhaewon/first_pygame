import pygame

from background import Background
from boss import Boss
from player import Player
from enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("myFirst Game")

background = Background(screen=screen)
player = Player(screen=screen)
enemies = tuple(Enemy(screen=screen) for _ in range(10))
boss = Boss(screen=screen)

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                is_running = False
            if event.key == pygame.K_a:
                player.is_attack = True
            if event.key == pygame.K_RIGHT:
                player.move_flag['right'] = True
            if event.key == pygame.K_LEFT:
                player.move_flag['left'] = True
            if event.key == pygame.K_UP:
                player.move_flag['up'] = True
            if event.key == pygame.K_DOWN:
                player.move_flag['down'] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.is_attack = False
            if event.key == pygame.K_RIGHT:
                player.move_flag['right'] = False
            if event.key == pygame.K_LEFT:
                player.move_flag['left'] = False
            if event.key == pygame.K_UP:
                player.move_flag['up'] = False
            if event.key == pygame.K_DOWN:
                player.move_flag['down'] = False

    background.draw()
    background.update()
    player.draw()
    player.update()
    player.animation()
    for enemy in enemies:
        enemy.draw()
        enemy.update()
    boss.draw()
    boss.animation()
    pygame.display.update()
