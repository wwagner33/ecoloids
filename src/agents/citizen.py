import pygame
from environment.grid import grid_to_iso

class Citizen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        # Implement movement logic
        pass

    def draw(self, screen, grid_size):
        iso_x, iso_y = grid_to_iso(self.x, self.y)
        pygame.draw.circle(screen, (0, 0, 255), (iso_x + grid_size // 2, iso_y + grid_size // 2), 10)
