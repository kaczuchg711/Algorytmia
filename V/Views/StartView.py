import pygame

from M.Button import Button
from V.Views.BasicView import BasicView
from V.Views.DijkstraView import DijkstraView


class StartView(BasicView):
    class ClickController:
        def __call__(self, event, view):
            if event.type == pygame.MOUSEBUTTONUP:
                for sprite in view.sprites:
                    x, y = event.pos
                    print(x, y)
                    if sprite.rect.collidepoint(x, y):
                        try:
                            view.changer.change_view("DijkstraView")
                        except KeyError:
                            view.changer.views["DijkstraView"] = DijkstraView(view.changer)
                            view.changer.change_view("DijkstraView")

    def __init__(self, changer):
        super().__init__()
        self.changer = changer
        self.sprites = [Button("siema", 10, 10, 100, 100)]
        self.controllers = [self.ClickController()]

    def draw_elements(self, surface):
        for element in self.sprites:
            element.draw(surface)
            element.update()

    def run_controllers(self, event):
        for controller in self.controllers:
            controller(event, self)
