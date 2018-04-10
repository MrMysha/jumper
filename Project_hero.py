import pygame
class Hero():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("images/Hero.png")
        self.image = pygame.transform.scale(self.image,(130, 117))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx+=3
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.rect.centerx-=3
    def blitme(self):
        self.screen.blit(self.image, self.rect)