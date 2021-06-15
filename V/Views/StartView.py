import pygame

from V.elements.FreeText import FreeText
from V.elements.TextButton import TextButton
from V.Views.BasicView import BasicView
from V.Views.DijkstraView import DijkstraView
from static import screen


class StartView(BasicView):
    class ClickController:
        def __call__(self, event, view):
            if event.type == pygame.MOUSEBUTTONUP:
                for sprite in view.sprites:
                    x, y = event.pos
                    try:
                        if sprite.rect.collidepoint(x, y):
                            if sprite.text == "Dijkstra":
                                try:
                                    view.changer.change_view("DijkstraView")
                                except KeyError:
                                    view.changer.views["DijkstraView"] = DijkstraView(view.changer)
                                    view.changer.change_view("DijkstraView")
                    except AttributeError:
                        pass


    def __init__(self, changer):
        super().__init__(changer)
        self._init_buttons()
        self.controllers = [self.ClickController()]

    def _init_buttons(self):

        self.sprites = [FreeText("Algorytmia", int(screen.rect.height * 0.2),
                                 screen.rect.centerx - (screen.rect.height * 0.2) * 4.9/ 2,
                                 screen.rect.centery - screen.rect.height * 0.9 / 2),
                        FreeText("Wizualizator algorytmów", int(screen.rect.height * 0.05),
                                 screen.rect.centerx - screen.rect.width * 0.30/ 2,
                                 screen.rect.centery - screen.rect.height * 0.3 / 2),
                        TextButton("Dijkstra", "Dijkstra", screen.rect.centerx - screen.rect.width * 0.2 / 2,
                                   screen.rect.centery - screen.rect.height * 0.1 / 2, screen.rect.width * 0.2,
                                   screen.rect.height * 0.1)]

    def draw_elements(self):
        for element in self.sprites:
            element.draw(self.changer.surface)
            element.update()

    def run_controllers(self, event):
        for controller in self.controllers:
            controller(event, self)
