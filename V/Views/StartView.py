import pygame

from V.Views.BasicView import BasicView


class StartView(BasicView):

    def drawElements(self, surface):
        for element in self.sprites:
            element.draw(surface)
            element.update()
