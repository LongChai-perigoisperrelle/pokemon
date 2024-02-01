import pygame
import sys

pygame.init()

largeur = 736
hauteur = 420
fenetre = pygame.display.set_mode((largeur, hauteur))

fond = pygame.image.load("image/boule.jpg")

# Charger la musique de fond
pygame.mixer.music.load("image/Main Menu - Pokémon HOME (1).mp3")
pygame.mixer.music.play(-1)  # -1 pour la lecture en boucle

# Fonction pour afficher le menu
def afficher_menu():
    # Vous pouvez personnaliser le menu ici
    menu_font = pygame.font.Font(None, 36)
    titre_menu = menu_font.render("Menu", True, (255, 255, 255))
    nouvelle_partie = menu_font.render("1. Nouvelle Partie", True, (255, 255, 255))
    quitter_jeu = menu_font.render("2. Quitter le Jeu", True, (255, 255, 255))

    fenetre.blit(titre_menu, (largeur // 2 - titre_menu.get_width() // 2, 100))
    fenetre.blit(nouvelle_partie, (largeur // 2 - nouvelle_partie.get_width() // 2, 200))
    fenetre.blit(quitter_jeu, (largeur // 2 - quitter_jeu.get_width() // 2, 250))

# Boucle principale
en_cours = True
clock = pygame.time.Clock()

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    fenetre.blit(fond, (0, 0))

    # Appel de la fonction pour afficher le menu
    afficher_menu()

    pygame.display.flip()

    clock.tick(60)  # Limiter la fréquence d'images pour éviter une exécution trop rapide

pygame.mixer.music.stop()  # Arrêter la musique de fond
pygame.quit()
sys.exit()
