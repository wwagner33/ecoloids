import pygame

class Building:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, grid_size):
        pygame.draw.rect(screen, (200, 200, 200), (self.x * grid_size, self.y * grid_size, grid_size, grid_size))
