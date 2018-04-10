import pygame


class FallObject(object):
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("images/Hero.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.top

    def blitme(self):
        self.screen.blit(self.image, self.rect)
