import pygame

from M.Node import Node
from V.Views.BasicView import BasicView


class GraphView(BasicView):
    class ClickController:
        def __call__(self, event, view):
            if event.type == pygame.MOUSEBUTTONUP:
                if isinstance(view, GraphView):
                    pos = pygame.mouse.get_pos()
                    if event.button == 1:
                        view.add_element(Node(pos[0], pos[1]))
                    elif event.button == 3:
                        view.remove_element(pos)

    def __init__(self):
        super().__init__()
        self.controllers = [self.ClickController()]
        self.isInEditMode = False

    def add_element(self, sprite: pygame.sprite.Sprite):
        self.sprites.append(sprite)

    def remove_element(self, pos):
        clicked_sprites = [s for s in self.sprites if s.rect.collidepoint(pos)]
        try:
            self.sprites.remove(clicked_sprites[-1])
        except(IndexError):
            pass

    def run_controllers(self, event):
        for controller in self.controllers:
            controller(event, self)
