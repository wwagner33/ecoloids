import pygame
from agents.citizen import Citizen
from agents.building import Building
from agents.nature_element import NatureElement

class Simulation:
    def __init__(self, grid, config):
        self.grid = grid
        self.config = config
        self.screen = pygame.display.set_mode((config['SCREEN_WIDTH'], config['SCREEN_HEIGHT']))
        self.clock = pygame.time.Clock()
        self.agents = [
            Citizen(5, 5),
            Building(10, 10),
            NatureElement(15, 15)
        ]
        self.map_data = self.grid.load_terrain('data/map_data.json')

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((0, 0, 0))  # Clear screen
            self.grid.draw(self.screen, self.map_data)
            for agent in self.agents:
                agent.draw(self.screen, self.config['grid_size'])

            pygame.display.flip()
            self.clock.tick(self.config['MAX_FPS'])

        pygame.quit()
