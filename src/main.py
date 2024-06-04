import pygame
from environment.grid import Grid
from agents.citizen import Citizen
from agents.building import Building
from agents.nature_element import NatureElement
import json

def main():
    # Load configuration
    with open('data/config.json') as f:
        config = json.load(f)

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((config['window_width'], config['window_height']))
    pygame.display.set_caption("Ecoloids: Ecological Simulations")

    # Create grid
    grid = Grid(config['window_width'], config['window_height'], config['grid_size'])

    # Load terrain
    grid.load_terrain('data/map_data.json')

    # Create agents
    agents = [
        Citizen(5, 5),
        Building(10, 10),
        NatureElement(15, 15),
    ]

    running = True
    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw grid and agents
        grid.draw(screen)
        for agent in agents:
            agent.draw(screen, config['grid_size'])

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
