import pygame
from pygame.sprite import AbstractGroup


class Node(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.color = pygame.Color(255, 255, 255)
        self.radius = 30

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, [self.x, self.y], self.radius)
