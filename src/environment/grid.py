import pygame
import json
from src.utils import load_all_images

TILE_WIDTH = 64
TILE_HEIGHT = 32

def grid_to_iso(x, y):
    iso_x = (x - y) * TILE_WIDTH // 2
    iso_y = (x + y) * TILE_HEIGHT // 2
    return iso_x, iso_y

class Grid:
    def __init__(self, width, height, grid_size):
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.grid = [[None for _ in range(width // grid_size)] for _ in range(height // grid_size)]
        self.tile_images, self.object_images, self.agent_images = load_all_images()

    def draw(self, screen, map_data):
        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                iso_x, iso_y = grid_to_iso(x, y)
                screen.blit(self.tile_images[tile], (iso_x, iso_y))

    def load_terrain(self, map_file):
        with open(map_file) as f:
            map_data = json.load(f)
        return map_data["terrain"]
