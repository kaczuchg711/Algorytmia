from pygame.sprite import Sprite
from pygame import Color, Rect, draw, font


class Button(Sprite):
    def __init__(self, text, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.color = Color(200, 200, 200)
        self.width = width
        self.height = height
        self.rect = Rect(self.x, self.y, width, height)
        self.text = text

    def draw(self, surface):
        draw.rect(surface, self.color, self)
        myfont = font.SysFont('Comic Sans MS', 16)
        textsurface = myfont.render('Text', False, (0, 0, 0))
        TextLeftRightCor = (self.rect.center[0]-textsurface.get_width()/2, self.rect.center[1]-textsurface.get_height()/2)

        surface.blit(textsurface, TextLeftRightCor)
