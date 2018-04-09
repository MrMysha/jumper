import pygame
class Background():
    def __init__(self,screen):
        self.screen=screen
        self.bg_img=pygame.image.load("images/Background.jpg").convert()
        #self.bg_img=pygame.transform.scale(self.bg_img,(1920, 1080))#
        self.rect_img = self.bg_img.get_rect()
    def update(self):
        self.screen.blit(self.bg_img, self.rect_img)