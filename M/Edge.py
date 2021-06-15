from typing import overload, Union, List, Tuple

import pygame

from pygame.sprite import Sprite
from pygame import color


DISTANCE_FROM_EDGE = 1000

class Edge(Sprite):
    class EdgeRect(pygame.Rect):
        def __init__(self, pos1, pos2, name="--"):
            self.pos1 = pos1
            self.pos2 = pos2

        def collidepoint(self, pos: tuple, **kwargs):
            def is_on(a, b, c):
                "Return true iff point c intersects the line segment from a to b."
                # (or the degenerate case that all 3 points are coincident)
                return (collinear(a, b, c)
                        and (within(a.x, c.x, b.x) if a.x != b.x else
                             within(a.y, c.y, b.y)))

            def collinear(a, b, c):
                "Return true iff a, b, and c all lie on the same line."

                #     print((b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y))
                return abs((b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)) < DISTANCE_FROM_EDGE

            def within(p, q, r):
                "Return true iff q is between p and r (inclusive)."
                return p <= q <= r or r <= q <= p

                # a = (self.pos2[1] - self.pos1[1]) / (self.pos2[0] - self.pos1[0]) if (self.pos2[0] - self.pos1[0]) else 0
                # b = self.pos1[1] - a * self.pos1[0]
                # x = pos[0]
                # y = pos[1]
                #
                # if self._check_point_in_rect(pos) and (a * x + b - y > - 20 and a * x + b - y < 20):
                #     return True
            return is_on(Point(self.pos1[0], self.pos1[1]), Point(self.pos2[0], self.pos2[1]), Point(pos[0], pos[1]))

        def _check_point_in_rect(self, pos):
            #         todo
            return True

    def __init__(self, node1, node2):
        super().__init__()
        self.target = 1
        self.node1 = node1
        self.node2 = node2
        node1.edges.append(self)
        node2.edges.append(self)
        self.rect = self.EdgeRect(self.node1.rect.center, self.node2.rect.center, node1.name + node2.name)
        self.weight = None
        self.color = (255, 255, 255)
        self.selectedColor = (0, 255, 0)
        self.selected = False

    def draw(self, surface):
        lineSize = 10
        if self.selected:
            pygame.draw.line(surface, self.selectedColor, self.node1.rect.center, self.node2.rect.center, lineSize)
        else:
            pygame.draw.line(surface, self.color, self.node1.rect.center, self.node2.rect.center, lineSize)

        if self.weight is not None:



            font = pygame.font.SysFont('Times New Roman', 24)

            textsurface = font.render(str(self.weight), False, (0, 200, 255))
            TextLeftRightCor = (
            (self.rect.pos1[0] + self.rect.pos2[0]) / 2 - font.get_height() * 0.1, (self.rect.pos1[1] + self.rect.pos2[1]) / 2 - lineSize * 3 + font.get_height() * 0.70)
            pygame.draw.ellipse(surface, (160,160,160),pygame.Rect((TextLeftRightCor[0] - 8,TextLeftRightCor[1]), (len(str(self.weight))* 18 + 10, 24)))
            surface.blit(textsurface, TextLeftRightCor)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

