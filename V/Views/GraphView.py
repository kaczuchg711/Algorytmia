import pygame

from V.Views.BasicView import BasicView


class GraphView(BasicView):

    def __init__(self):
        super().__init__()
        self.isInEditMode = False

    def add_element(self, sprite: pygame.sprite.Sprite):
        self.sprites.append(sprite)

    def remove_element(self, pos):
        print(self.sprites)
        clicked_sprites = [s for s in self.sprites if s.rect.collidepoint(pos)]
        try:
            self.sprites.remove(clicked_sprites[-1])
        except(IndexError):
            pass
