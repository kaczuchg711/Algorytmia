from random import random

import pygame
from pygame.sprite import AbstractGroup


class Node(pygame.sprite.Sprite):
    alfabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "W",
               "Y", "Z")
    count = 0

    @classmethod
    def incr(cls):
        cls.count += 1

    def __init__(self, x, y):
        super().__init__()
        self.name = self.alfabet[self.count]
        self.incr()
        self.x = x
        self.y = y
        self.color = pygame.Color(255,255,255)
        self.radius = 30
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self, surface):
        myfont = pygame.font.SysFont('Times New Roman', 24)
        textsurface = myfont.render(self.name, False, (0, 0, 0))
        TextLeftRightCor = (self.rect.center[0]-textsurface.get_width()/2, self.rect.center[1]-textsurface.get_height()/2)
        pygame.draw.circle(surface, self.color, [self.x, self.y], self.radius)
        surface.blit(textsurface, TextLeftRightCor)
