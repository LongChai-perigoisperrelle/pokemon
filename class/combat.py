import pygame
import sys 
import json
import os

with open('class/pokedex.json','r') as file :
     pokemon_data = json.load(file)

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pokémon Game")
# Charger les images des Pokémon dans un dictionnaire
pokemon_images = {}
for pokemon in pokemon_data:
    image_path = os.path.join(os.getcwd(), pokemon["img"])
    if os.path.exists(image_path):
        pokemon_images[pokemon["nom"]] = pygame.image.load(image_path)
    else:
        print(f"Erreur : Le fichier image {image_path} n'existe pas.")


class Combat:
    def __init__(self, player_pokemon, opponent_pokemon):
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = opponent_pokemon

    def calculate_damage(self, attacker, defender):
        damage = (attacker["attaque"] / defender["defense"]) * 10
        return damage

    def fight(self):
        player_damage = self.calculate_damage(self.player_pokemon, self.opponent_pokemon)
        opponent_damage = self.calculate_damage(self.opponent_pokemon, self.player_pokemon)

        self.opponent_pokemon["hp"] -= player_damage
        self.player_pokemon["hp"] -= opponent_damage

        print(f"{self.player_pokemon['nom']} inflige {player_damage} dégat à {self.opponent_pokemon['nom']}.")
        print(f"{self.opponent_pokemon['nom']} inflige {opponent_damage} dégat à {self.player_pokemon['nom']}.")

        if self.opponent_pokemon["hp"] <= 0:
            print(f"{self.opponent_pokemon['nom']} a été vaincu !")
        elif self.player_pokemon["hp"] <= 0:
            print(f"{self.player_pokemon['nom']} a été vaincu !")


player_pokemon = {
    "nom": "Pikatchu",
    "hp": 35,
    "attaque": 55,
    "defense": 40,
    "type": ["Elecric"]
}
opponent_pokemon = {
    "nom": "Eevee",
    "hp": 55,
    "attaque": 55,
    "defense": 50,
    "type": ["Nature"]
}
combat = Combat(player_pokemon, opponent_pokemon)
# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacer l'écran
    screen.fill((255, 255, 255))

    # Afficher les images des Pokémon
    x_player = 100
    x_opponent = 500
    y = 200

    screen.blit(pokemon_images[player_pokemon["nom"]], (x_player, y))
    screen.blit(pokemon_images[opponent_pokemon["nom"]], (x_opponent, y))

    # Afficher le résultat du combat
    combat.fight()

    # Mettre à jour l'écran
    pygame.display.flip()

 # Quitter Pygame
pygame.quit()
sys.exit()

