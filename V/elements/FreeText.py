import pygame
from pygame.sprite import Sprite


class FreeText(Sprite):
    def __init__(self,text,x,y):
        super().__init__()
        self.text = text
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont('Times New Roman', 24)

    def draw(self, surface):
        textsurface = self.font.render(self.text, False, (255, 255, 255))
        TextLeftRightCor = (self.x, self.y)
        surface.blit(textsurface, TextLeftRightCor)

    def set_activity(self, fun):
        activity = fun
