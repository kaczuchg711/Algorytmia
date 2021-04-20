import pygame
from pygame.sprite import Sprite
from pygame import Color, Rect, draw, font

from V.elements.Button import Button


class ImageButton(Button):
    def __init__(self, image, name, x, y, width, height):
        super().__init__(name, x, y, width, height)
        self.image = pygame.transform.scale(image, (width, height))

    def draw(self, surface):
        surface.blit(self.image, [self.x, self.y])
