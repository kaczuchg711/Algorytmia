import pygame

from M.Node import Node
from V.Views.BasicView import BasicView
from V.elements.Button import Button
from V.elements.ImageButton import ImageButton
from static import screen


class GraphView(BasicView):
    class ClickController:
        def __call__(self, event, view):
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                buttons = [button for button in view.sprites if isinstance(button, Button)]

                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        if event.button == 1 and button.name == "editButton" and button.rect.collidepoint(event.pos):
                            if view.isInEditMode:
                                view.isInEditMode = False
                                button.image.set_alpha(50)
                            else:
                                view.isInEditMode = True
                                button.image.set_alpha(255)

                    else:
                        if event.button == 1 and view.isInEditMode:
                            view.add_element(Node(pos[0], pos[1]))
                        elif event.button == 3 and view.isInEditMode:
                            view.remove_element(pos)

    def __init__(self):
        super().__init__()
        self.controllers = [self.ClickController()]
        editIcon = pygame.image.load('icons\edit_icon.png').convert_alpha()
        editIcon.set_alpha(50)
        editButton = ImageButton(editIcon, "editButton", screen.rect.width - 0.05 * screen.rect.width, 0, 50, 50)
        self.sprites.append(editButton)
        self.isInEditMode = False

    def add_element(self, sprite):
        self.sprites.append(sprite)

    def remove_element(self, pos):
        clicked_sprites = [s for s in self.sprites if s.rect.collidepoint(pos)]
        try:
            self.sprites.remove(clicked_sprites[-1])
        except(IndexError):
            pass

    def run_controllers(self, event):
        for controller in self.controllers:
            controller(event, self)
