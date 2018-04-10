import pygame


class Hero(object):
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("images/Hero.png")
<<<<<<< HEAD
        self.image = pygame.transform.scale(self.image,(130, 117))
=======
        self.image = pygame.transform.scale(self.image, (50, 50))
>>>>>>> 148da33282a6b1bd6fe8e4513176fa2aeffc4eba
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
<<<<<<< HEAD
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx+=3
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.rect.centerx-=3
=======
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 1
        if self.moving_up:
            self.rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1

>>>>>>> 148da33282a6b1bd6fe8e4513176fa2aeffc4eba
    def blitme(self):
        self.screen.blit(self.image, self.rect)
