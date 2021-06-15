import pygame
from pygame import Rect
from pygame.sprite import Sprite


class Screen(Sprite):
    def __init__(self):
        super().__init__()
        self.rect = Rect(0, 0, 1600, 900)


screen = Screen()

numeric_keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_KP0,
                pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5,
                pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]

numeric_keys_dict = {"48": 0, "49": 1, "50": 2, "51": 3, "52": 4, "53": 5, "54": 6, "55": 7, "56": 8, "57": 9,
                     "1073741922": 0, "1073741913": 1, "1073741914": 2, "1073741915": 3, "1073741916": 4,
                     "1073741917": 5, "1073741918": 6, "1073741919": 7, "1073741920": 8, "1073741921": 9}
