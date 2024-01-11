import pygame
import json
import os

with open('class/pokedex.json', 'r') as file:
    pokemon_data = json.load(file)

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pokémon Game")

pokemon_images = []
for pokemon in pokemon_data:
    image_path = os.path.join(os.getcwd(), pokemon["img"])
    if os.path.exists(image_path):
        pokemon_images.append(pygame.image.load(image_path))
    else:
        print(f"Erreur : Le fichier image {image_path} n'existe pas.")

class GUI:
    def __init__(self):
        self.selected_pokemon = None

    def select_pokemon(self, mouse_pos):
        for index, image in enumerate(pokemon_images):
            x = index * 200
            y = 0
            rect = image.get_rect(topleft=(x, y))
            if rect.collidepoint(mouse_pos):
                self.selected_pokemon = pokemon_data[index]
                print(f"Pokemon sélectionné : {self.selected_pokemon['nom']}")

    def draw_pokemon_name(self, screen, pokemon_data):
        font = pygame.font.Font(None, 24)
        for index, pokemon in enumerate(pokemon_data):
            x = index * 200
            y = 200
            text_surface = font.render(pokemon["nom"], True, (0, 0, 0))
            screen.blit(text_surface, (x, y))

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            gui.select_pokemon(event.pos)

    
    screen.fill((255, 255, 255))

    # Dessiner les images de tous les Pokémon
    for index, image in enumerate(pokemon_images):
        x = index * 200
        y = 0
        screen.blit(image, (x, y))

    # Dessiner les noms des Pokémon
    gui = GUI()
    gui.draw_pokemon_name(screen, pokemon_data)

    
    pygame.display.flip()


pygame.quit()





