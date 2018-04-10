import pygame
from Project_settings import Settings
from Project_hero import Hero
from Project_background import Background
import Project_game_function


def init_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Project")
    hero = Hero(screen)
    background = Background(screen)

    while True:

        Project_game_function.check_events(hero)
        hero.update()
        Project_game_function.update_screen(background, hero)


init_game()
