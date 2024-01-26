import pygame
import sys
import json
import os

pygame.init()

# Initialisation de l'écran
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jeu Pokémon")

# Chargement de l'image de fond
background_image = pygame.image.load("image/FOND.png").convert()
largeur = 800
hauteur = 600
background_image = pygame.transform.scale(background_image, (largeur, hauteur))

# Dictionnaire pour stocker les images des Pokémon
pokemon_images = {}
with open('class/pokedex.json', 'r') as file:
    pokemon_data = json.load(file)
    for pokemon in pokemon_data:
        chemin_image = os.path.join(os.getcwd(), pokemon["img"])
        if os.path.exists(chemin_image):
            pokemon_images[pokemon["nom"]] = pygame.image.load(chemin_image)
        else:
            print(f"Erreur : Le fichier image {chemin_image} n'existe pas.")

class Combat:
    def __init__(self, pokemon_joueur, pokemon_adversaire):
        self.pokemon_joueur = pokemon_joueur
        self.pokemon_adversaire = pokemon_adversaire

    def calculer_degats(self, attaquant, defenseur):
        degats = (attaquant["attaque"] / defenseur["defense"]) * 10
        return degats

    def dessiner_barres_de_vie(self, x_joueur, y_joueur, x_adversaire, y_adversaire):
        largeur_barre_de_vie = 100
        hauteur_barre_de_vie = 30

        # Barre de vie du joueur
        pourcentage_vie_joueur = self.pokemon_joueur["hp"] / self.pokemon_joueur.get("max_hp", self.pokemon_joueur["hp"])
        couleur_joueur = (0, 255, 0) if pourcentage_vie_joueur > 0.6 else (255, 255, 0) if pourcentage_vie_joueur > 0.3 else (255, 0, 0)
        pygame.draw.rect(screen, couleur_joueur, (x_joueur, y_joueur - 20, largeur_barre_de_vie * pourcentage_vie_joueur, hauteur_barre_de_vie))

        # Barre de vie de l'adversaire
        pourcentage_vie_adversaire = self.pokemon_adversaire["hp"] / self.pokemon_adversaire.get("max_hp", self.pokemon_adversaire["hp"])
        couleur_adversaire = (0, 255, 0) if pourcentage_vie_adversaire > 0.6 else (255, 255, 0) if pourcentage_vie_adversaire > 0.3 else (255, 0, 0)
        pygame.draw.rect(screen, couleur_adversaire, (x_adversaire, y_adversaire - 20, largeur_barre_de_vie * pourcentage_vie_adversaire, hauteur_barre_de_vie))

    def combat(self):
        degats_joueur = self.calculer_degats(self.pokemon_joueur, self.pokemon_adversaire)
        degats_adversaire = self.calculer_degats(self.pokemon_adversaire, self.pokemon_joueur)

        self.pokemon_adversaire["hp"] -= degats_joueur
        self.pokemon_joueur["hp"] -= degats_adversaire

        print(f"{self.pokemon_joueur['nom']} inflige {degats_joueur} dégât à {self.pokemon_adversaire['nom']}.")
        print(f"{self.pokemon_adversaire['nom']} inflige {degats_adversaire} dégât à {self.pokemon_joueur['nom']}.")

        if self.pokemon_adversaire["hp"] <= 0:
            print(f"{self.pokemon_adversaire['nom']} a été vaincu !")
        elif self.pokemon_joueur["hp"] <= 0:
            print(f"{self.pokemon_joueur['nom']} a été vaincu !")

    def afficher_vainqueur(self, vainqueur):
        texte = font.render(f"{vainqueur['nom']} est le vainqueur !", True, (255, 255, 255))
        rect_texte = texte.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(texte, rect_texte)
        pygame.display.flip()
        pygame.time.delay(3000)

# Données du Pokémon du joueur
pokemon_joueur = {
    "img": "image/Charmander.png",
    "nom": "Charmander",
    "hp": 45,
    "attaque": 49,
    "defense": 49,
    "type": ["Feu"]
}

# Données du Pokémon adverse
pokemon_adversaire = {
    "img": "image/Eevee.png",
    "nom": "Eevee",
    "hp": 55,
    "attaque": 55,
    "defense": 50,
    "type": ["Nature"]
}

combat = Combat(pokemon_joueur, pokemon_adversaire)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))

    x_joueur = 100
    x_adversaire = 500
    y_joueur = 200
    y_adversaire = 400

    screen.blit(pokemon_images[pokemon_joueur["nom"]], (x_joueur, y_adversaire))
    screen.blit(pokemon_images[pokemon_adversaire["nom"]], (x_adversaire, y_joueur))

    combat.dessiner_barres_de_vie(x_joueur, y_joueur, x_adversaire, y_adversaire)

    pygame.display.flip()

combat.combat()

if pokemon_joueur["hp"] <= 0:
    combat.afficher_vainqueur(pokemon_adversaire)
elif pokemon_adversaire["hp"] <= 0:
    combat.afficher_vainqueur(pokemon_joueur)

pygame.quit()
sys.exit()

