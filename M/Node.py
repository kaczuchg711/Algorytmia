from random import random

import pygame
from pygame.sprite import AbstractGroup


class Node(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.color = pygame.Color(int(random() * 100), int(random() * 100), int(random() * 100))
        self.radius = 30
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, [self.x, self.y], self.radius)
