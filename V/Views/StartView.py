import pygame

from M.Node import Node


class StartView:

    def __init__(self):
        self.sprites = []

    def drawElements(self, surface):
        for element in self.sprites:
            element.draw(surface)
            element.update()

    def add_element(self, sprite: pygame.sprite.Sprite):
        self.sprites.append(sprite)
