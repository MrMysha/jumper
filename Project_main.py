import pygame
import time
from Project_settings import Settings
from Project_hero import Hero
from Project_background import Background
import Project_game_function as g_f
from Projet_enemy import Alien
from pygame.sprite import Group

def init_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Project")
    hero = Hero(settings, screen)
    aliens = Group()

    background = Background(screen)
    g_f.create_fleet(settings, screen, aliens)

    while True:
        g_f.check_events(hero)

        hero.update()

        g_f.update_screen(background, hero, aliens, screen)

        g_f.if_create_fleet_down(settings, screen, aliens, hero)


        time.sleep(0.0005)


init_game()
