from typing import overload, Union, List, Tuple

import pygame

from pygame.sprite import Sprite


class Edge(Sprite):
    class EdgeRect(pygame.Rect):
        def __init__(self, pos1, pos2):
            self.pos1 = pos1
            self.pos2 = pos2

        def collidepoint(self, pos: tuple, **kwargs):
            a = (self.pos2[1] - self.pos1[1]) / (self.pos2[0] - self.pos1[0])
            b = self.pos1[1] - a * self.pos1[0]
            x = pos[0]
            y = pos[1]

            if self._check_point_in_rect(pos) and (a * x + b - y > - 20 and a * x + b - y < 20):
                return True

        def _check_point_in_rect(self, pos):
            #         todo self
            return True

    def __init__(self, node1, node2):
        super().__init__()
        self.target = 1
        self.node1 = node1
        self.node2 = node2
        self.rect = self.EdgeRect(self.node1.rect.center, self.node2.rect.center)
        self.weight = None

    def draw(self, surface):
        pygame.draw.line(surface, (255, 255, 255), self.node1.rect.center, self.node2.rect.center, 10)
