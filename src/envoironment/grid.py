import pygame
import json

class Grid:
    def __init__(self, width, height, grid_size):
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.grid = [[None for _ in range(width // grid_size)] for _ in range(height // grid_size)]

    def draw(self, screen):
        for y in range(self.height // self.grid_size):
            for x in range(self.width // self.grid_size):
                rect = pygame.Rect(x * self.grid_size, y * self.grid_size, self.grid_size, self.grid_size)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)

    def load_terrain(self, map_file):
        with open(map_file) as f:
            map_data = json.load(f)
        # Implement terrain loading logic based on map_data
