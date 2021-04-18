import pygame

from M.Node import Node
from V.Views.GraphView import GraphView


class ClickController:
    def __call__(self, event, sprites, view):
        if event.type == pygame.MOUSEBUTTONUP:
            if isinstance(view, GraphView):
                pos = pygame.mouse.get_pos()
                if event.button == 1:
                    view.add_element(Node(pos[0], pos[1]))
                elif event.button == 3:
                    view.remove_element(pos)
