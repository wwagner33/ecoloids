import pygame

class Citizen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        # Implement movement logic
        pass

    def draw(self, screen, grid_size):
        pygame.draw.circle(screen, (0, 0, 255), (self.x * grid_size + grid_size // 2, self.y * grid_size + grid_size // 2), grid_size // 2)
