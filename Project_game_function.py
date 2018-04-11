import pygame
import sys
from Projet_enemy import Alien
from random import randint

def check_events(hero):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, hero)
        elif event.type == pygame.KEYUP:
            chek_keyup_events(event, hero)


def update_screen(background, hero, aliens, screen):
    aliens.update()
    background.update()
    hero.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def check_keydown_events(event, hero):
    if event.key == pygame.K_RIGHT:
        hero.moving_right = True
    if event.key == pygame.K_LEFT:
        hero.moving_left = True
    


def chek_keyup_events(event, hero):
    if event.key == pygame.K_RIGHT:
        hero.moving_right = False
    if event.key == pygame.K_LEFT:
        hero.moving_left = False



def if_create_fleet_down(settings, screen,aliens,hero):
    for alien in aliens.copy():
        if alien.rect.bottom == alien.screen_rect.bottom:
            aliens.empty()
            create_fleet(settings, screen, aliens)

    for alien in aliens.copy():

        x_1 = hero.rect.x - hero.rect.width / 2
        x_2 = hero.rect.x + hero.rect.width / 2


        for alien_rect_x in range(int(x_1),int(x_2)):
            if alien.rect.x == alien_rect_x and alien.rect.y == hero.rect.top:
                print('Loser')
                sys.exit()


        '''if alien.rect.x == range((hero.rect.x - hero.rect.width / 2),(hero.rect.x + hero.rect.width / 2))  and alien.rect.y >= hero.rect.top :
            print('2')
            #sys.exit()'''

def create_fleet(settings, screen, aliens):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width

    number_aliens_x = 1
    num = randint(0,10)
    for alien_number in range(number_aliens_x):

        alien = Alien(settings, screen)
        alien.rect.x = alien_width*num
        aliens.add(alien)


