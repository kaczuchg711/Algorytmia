from pygame.sprite import Sprite
from pygame import Color, Rect, draw, font

from V.elements.Button import Button


class TextButton(Button):
    def __init__(self, text, name, x, y, width, height):
        super().__init__(name, x, y, width, height)
        self.color = Color(200, 200, 200)
        self.text = text

    def draw(self, surface):
        draw.rect(surface, self.color, self.rect)
        myfont = font.SysFont('Times New Roman', 24)
        textsurface = myfont.render(self.text, False, (0, 0, 0))
        TextLeftRightCor = (self.rect.center[0]-textsurface.get_width()/2, self.rect.center[1]-textsurface.get_height()/2)

        surface.blit(textsurface, TextLeftRightCor)
