import pygame
import sys


def check_events(hero):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, hero)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, hero)


def update_screen(background, hero, obj):
    background.update()
    hero.blitme()
    obj.blitme()
    pygame.display.flip()


def check_keydown_events(event, hero):
    if event.key == pygame.K_RIGHT:
        hero.moving_right = True
    if event.key == pygame.K_LEFT:
        hero.moving_left = True


def check_keyup_events(event, hero):
    if event.key == pygame.K_RIGHT:
        hero.moving_right = False
    if event.key == pygame.K_LEFT:
        hero.moving_left = False
