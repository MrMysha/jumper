import pygame
import sys


def check_events(hero):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, hero)
        elif event.type == pygame.KEYUP:
            chek_keyup_events(event, hero)


def update_screen(background, hero):
    #  background.update()#
    background.update()
    hero.blitme()
    pygame.display.flip()


def check_keydown_events(event, hero):
    if event.key == pygame.K_RIGHT:
        hero.moving_right = True
    if event.key == pygame.K_LEFT:
        hero.moving_left = True
    if event.key == pygame.K_UP:
        hero.moving_up = True
    if event.key == pygame.K_DOWN:
        hero.moving_down = True


def chek_keyup_events(event, hero):
    if event.key == pygame.K_RIGHT:
        hero.moving_right = False
    if event.key == pygame.K_LEFT:
        hero.moving_left = False
    if event.key == pygame.K_UP:
        hero.moving_up = False
    if event.key == pygame.K_DOWN:
        hero.moving_down = False
