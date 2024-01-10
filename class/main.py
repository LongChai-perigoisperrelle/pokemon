import pygame

pygame.init()


largeur = 736
hauteur = 460
fenetre = pygame.display.set_mode((largeur, hauteur))


fond = pygame.image.load("image/boule.jpg")


en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False


    fenetre.blit(fond, (0, 0))


    pygame.display.flip()


pygame.quit()