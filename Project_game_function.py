import pygame,sys
def check_events(hero):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, hero)
        elif event.type == pygame.KEYUP:
            chek_keyup_events(event, hero)
def update_screen(background,hero):
    #background.update()#
    background.update()
    hero.blitme()
    pygame.display.flip()
def check_keydown_events(event,hero):
    if event.key == pygame.K_RIGHT:
        hero.moving_right = True
        hero.image = pygame.image.load("images/Hero.png")
        hero.image = pygame.transform.scale(hero.image, (130, 117))
    if event.key == pygame.K_LEFT:
        hero.moving_left = True
        hero.image = pygame.image.load("images/Hero_flip.png")
        hero.image = pygame.transform.scale(hero.image, (130, 117))
def chek_keyup_events(event,hero):
    if event.key == pygame.K_RIGHT:
        hero.moving_right = False
    if event.key == pygame.K_LEFT:
        hero.moving_left = False