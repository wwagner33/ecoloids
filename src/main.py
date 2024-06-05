import pygame
import sys
import json
from environment.grid import Grid
from simulation import Simulation

def main():
    # Load configuration
    with open('data/config.json') as f:
        config = json.load(f)

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((config['SCREEN_WIDTH'], config['SCREEN_HEIGHT']))
    pygame.display.set_caption("Ecoloids: Ecological Simulations")

    # Create grid and simulation
    grid = Grid(config['SCREEN_WIDTH'], config['SCREEN_HEIGHT'], config['grid_size'])
    simulation = Simulation(grid, config)

    # Run the simulation
    simulation.run()

if __name__ == "__main__":
    main()
