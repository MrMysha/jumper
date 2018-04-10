import pygame
<<<<<<< HEAD
class Background():
    def __init__(self,screen):
        self.screen=screen
        self.bg_img=pygame.image.load("images/Background.jpg").convert()
        self.bg_img=pygame.transform.scale(self.bg_img,(600, 950))
=======


class Background(object):
    def __init__(self, screen):
        self.screen = screen
        self.bg_img = pygame.image.load("images/background_1.jpg").convert()
        self.bg_img = pygame.transform.scale(self.bg_img, (800, 800))
>>>>>>> 148da33282a6b1bd6fe8e4513176fa2aeffc4eba
        self.rect_img = self.bg_img.get_rect()

    def update(self):
        self.screen.blit(self.bg_img, self.rect_img)
