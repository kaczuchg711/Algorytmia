from pygame import Rect
from pygame.sprite import Sprite

class Screen(Sprite):
    def __init__(self):
        super().__init__()
        self.rect = Rect(0, 0, 1600, 900)

screen = Screen()