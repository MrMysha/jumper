import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()
        self.image =  pygame.image.load('Projet_enemy.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()





    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.settings.alien_speed_factor






