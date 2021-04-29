import pygame

from M.Edge import Edge
from M.Node import Node
from V.Views.BasicView import BasicView
from V.elements.Button import Button
from V.elements.FreeText import FreeText
from V.elements.ImageButton import ImageButton
from static import screen, numeric_keys, numeric_keys_dict


class GraphView(BasicView):
    class ClickController:
        def __init__(self):
            self.firstSelectedNode = None
            self.lastCreatedEdge = None

        def __call__(self, event, view):
            # print("w ClickController")
            # # todo Edge weight
            edgeWasCreated = False
            nodes = [sprite for sprite in view.sprites if isinstance(sprite, Node)]

            for node in nodes:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and node.rect.collidepoint(
                        event.pos) and view.isInEditMode:
                    if self.firstSelectedNode is None and node is not self.firstSelectedNode:
                        self.firstSelectedNode = node
                    else:
                        self.lastCreatedEdge = Edge(self.firstSelectedNode, node)
                        view.sprites.append(FreeText("Input edge weight and press Enter", 10, 10))
                        view.sprites.append(self.lastCreatedEdge)
                        self.firstSelectedNode = None
                        edgeWasCreated = True
            #     if self.lastCreatedEdge is not None and self.lastCreatedEdge.weight is None:
            #         while not self.numberWasInput:
            #             print("while not self.numberWasInput:")
            #             for event in pygame.event.get():
            #                 if event.type == pygame.KEYDOWN:
            #                     print("Guzik został wciśnięty")
            #
            #                     if event.key in numeric_keys:
            #                         self.numberWasInput = True
            #                         print("Numeryczny guzik został wciśnięty")
            #                         self.numberForSetEdgeWeight += (str(numeric_keys_dict[str(event.key)]))
            #                         print(self.numberForSetEdgeWeight)
            #
            #                     keys = pygame.key.get_pressed()
            #                     if self.numberWasInput and (
            #                             event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN):
            #                         print("Enter został wciśnięty")
            #                         self.lastCreatedEdge.weight = int(self.numberForSetEdgeWeight)
            #
            #                         self.numberForSetEdgeWeight = str()
            #                         self.lastCreatedEdge = None
            #                         self.numberWasInput = False
            #

            #
            if event.type == pygame.MOUSEBUTTONDOWN and self.firstSelectedNode is None and not edgeWasCreated:
                pos = pygame.mouse.get_pos()
                buttons = [button for button in view.sprites if isinstance(button, ImageButton)]

                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        if event.button == 1:
                            self._turn_on_off_edit_mode(view, button)
                    else:
                        self._create_remove_node(event, view, pos)

        def _turn_on_off_edit_mode(self, view, button):
            if view.isInEditMode:
                view.isInEditMode = False
                button.image.set_alpha(50)
            else:
                view.isInEditMode = True
                button.image.set_alpha(255)

        def _create_remove_node(self, event, view, pos):
            if event.button == 1 and view.isInEditMode:
                view.add_element(Node(pos[0], pos[1]))
            elif event.button == 3 and view.isInEditMode:
                view.remove_element(pos)

    def __init__(self, changer):
        super().__init__(changer)
        self.controllers = [self.ClickController()]
        editIcon = pygame.image.load('icons\edit_icon.png').convert_alpha()
        editIcon.set_alpha(50)
        editButton = ImageButton(editIcon, screen.rect.width - 0.05 * screen.rect.width, 0, 50, 50)
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
