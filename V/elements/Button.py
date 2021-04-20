from pygame import Rect
from pygame.sprite import Sprite


class Button(Sprite):
    def __init__(self, name, x, y, width, height):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(self.x, self.y, width, height)
