import pygame
import sys
import json
import os

# Charger les données du Pokédex depuis le fichier pokedex.json
with open('class/pokedex.json', 'r') as file:
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


class PokemonSprite(pygame.sprite.Sprite):
    def __init__(self, pokemon, x, y):
        super().__init__()
        self.pokemon = pokemon
        self.image = pokemon_images[pokemon["nom"]]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.max_hp = pokemon["point_de_vie"]
        self.current_hp = self.max_hp

    def draw_health_bar(self, screen):
        bar_width = 60
        bar_height = 10
        bar_x = self.rect.x
        bar_y = self.rect.y - 15

        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))  
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, int(bar_width * (self.current_hp / self.max_hp)), bar_height)) 


class Combat:
    def __init__(self, player_pokemon, opponent_pokemon):
        self.player_sprite = PokemonSprite(player_pokemon, 100, 200)
        self.opponent_sprite = PokemonSprite(opponent_pokemon, 500, 200)

    def calculate_damage(self, attacker, defender):
        damage = (attacker["attaque"] / defender["defense"]) * 10
        return damage

    def fight(self):
        player_damage = self.calculate_damage(self.player_sprite.pokemon, self.opponent_sprite.pokemon)
        opponent_damage = self.calculate_damage(self.opponent_sprite.pokemon, self.player_sprite.pokemon)

        self.opponent_sprite.current_hp -= player_damage
        self.player_sprite.current_hp -= opponent_damage

        print(f"{self.player_sprite.pokemon['nom']} inflige {player_damage} dégât à {self.opponent_sprite.pokemon['nom']}.")
        print(f"{self.opponent_sprite.pokemon['nom']} inflige {opponent_damage} dégât à {self.player_sprite.pokemon['nom']}.")

    def draw_battle(self):
        screen.fill((255, 255, 255))

        # Afficher les images des Pokémon et leurs barres de vie
        screen.blit(self.player_sprite.image, self.player_sprite.rect)
        self.player_sprite.draw_health_bar(screen)

        screen.blit(self.opponent_sprite.image, self.opponent_sprite.rect)
        self.opponent_sprite.draw_health_bar(screen)

        pygame.display.flip()


# Pokémon de test
player_pokemon = {
    "img": "image/Charmander.png",
    "nom": "Charmander",
    "point_de_vie": 45,
    "attaque": 49,
    "defense": 49,
    "type": ["Feu"]
}

opponent_pokemon = {
    "img": "image/Eevee.png",
    "nom": "Eevee",
    "point_de_vie": 55,
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

    
    combat.draw_battle()
combat.fight()
pygame.quit()
sys.exit()
     
        
