import pygame

from M.Edge import Edge
from M.Node import Node
from M.Graph import Graph
from V.Views.BasicView import BasicView
from V.elements.Button import Button
from V.elements.FreeText import FreeText
from V.elements.ImageButton import ImageButton
from static import screen, numeric_keys, numeric_keys_dict


class GraphView(BasicView):
    class ClickController:
        def __init__(self):
            self.selectedNodes = []
            self.numberWasInput = False
            self.numberForSetEdgeWeight = str()
            self.InputNumberText = None

            self.dbclock = pygame.time.Clock()  # timmer do podwojengo klikniecia
            self.DOUBLECLICKTIME = 500  # czas do podwojnego klikniecia

            self.startSelectMode = False
            self.startSelected = False
            self.endSelectMode = False
            self.endSelected = False


        def __call__(self, event, view):

            if view.isInEditMode:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for node in view.graphHistory[view.pos].nodes:
                        if node.rect.collidepoint(event.pos):
                            if node not in self.selectedNodes and len(self.selectedNodes) < 2:
                                node.selected = True
                                self.selectedNodes.append(node)

                            if len(self.selectedNodes) == 2:
                                # todo sometimes the program doesn't print this text
                                self.InputNumberText = FreeText("Podaj wagę krawędzi i naciśnij Enter", 24,
                                                                screen.rect.centerx - 24 * 7, screen.rect.height * 0.01)
                                view.sprites.append(self.InputNumberText)

                if event.type == pygame.KEYDOWN and self.InputNumberText is not None:
                    if event.key in numeric_keys:
                        self.numberForSetEdgeWeight += (str(numeric_keys_dict[str(event.key)]))
                        self.numberWasInput = True

                if event.type == pygame.KEYDOWN and self.numberWasInput and (
                        event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN):

                    edge = Edge(self.selectedNodes[0], self.selectedNodes[1])
                    edge.weight = int(self.numberForSetEdgeWeight)

                    view.add_element(edge)

                    self.numberForSetEdgeWeight = str()
                    view.sprites.remove(self.InputNumberText)
                    self.InputNumberText = None
                    self.numberWasInput = False
                    for node in self.selectedNodes:
                        node.selected = False
                    self.selectedNodes.clear()

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        for node in view.graphHistory[0].nodes:
                            if node.start:
                                break
                        else:
                            #view.sprites.remove(self.InputNumberText)
                            self.InputNumberText = FreeText("Wskarz Start i naciśnij Enter", 24,
                                                            screen.rect.centerx - 24 * 7, screen.rect.height * 0.01)
                            view.sprites.append(self.InputNumberText)
                            self.startSelectMode = True

                        if self.startSelected and self.endSelected:
                            view.fill_history()
                            view.draw_graph()
                        # view.draw_route(view.graph, view.graph.nodes[0], view.graph.nodes[2])
                    elif event.key == pygame.K_LEFT:
                        view.rewind_history()
                    elif event.key == pygame.K_RIGHT:
                        view.fast_forward_history()

                    elif self.startSelectMode and (pygame.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN):
                        for node in view.graphHistory[0].nodes:
                            if node.selected:
                                node.start = True
                                node.selected = False
                                break
                        self.startSelectMode = False
                        view.sprites.remove(self.InputNumberText)
                        self.InputNumberText = FreeText("Wskarz Koniec i naciśnij Enter", 24,
                                                        screen.rect.centerx - 24 * 7, screen.rect.height * 0.01)
                        view.sprites.append(self.InputNumberText)
                        self.endSelectMode = True

                    elif self.endSelectMode and (pygame.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN):
                        flag = True
                        for node in view.graphHistory[0].nodes:
                            if node.selected:
                                n = node
                                node.selected = False
                                break
                        else:
                            flag = False
                        if flag:
                            self.endSelectMode = False
                            self.endSelected = True
                            view.sprites.remove(self.InputNumberText)
                            view.fill_history(n)
                            view.draw_graph()

            if self.startSelectMode or self.endSelectMode:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    print("ESC!")
                    for node in view.graphHistory[view.pos].nodes:
                        node.start = False
                        node.selected = False
                    print("ESC!")
                    self.startSelected = False
                    self.endSelected = False
                    self.endSelectMode = False
                    self.startSelectMode = False
                    view.sprites.remove(self.InputNumberText)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for node in view.graphHistory[view.pos].nodes:
                        node.selected = False

                    for node in view.graphHistory[view.pos].nodes:
                        if node.rect.collidepoint(event.pos):
                            node.selected = True

            elif not self.endSelected and event.type == pygame.MOUSEBUTTONDOWN and len(self.selectedNodes) == 0:
                pos = pygame.mouse.get_pos()
                buttons = [button for button in view.sprites if isinstance(button, ImageButton)]

                for button in buttons:
                    if button.rect.collidepoint(event.pos) and event.button == 1:
                        self._turn_on_off_edit_mode(view, button)
                        break
                else:
                    if self.dbclock.tick() < self.DOUBLECLICKTIME:
                        self._create_remove_node(event, view, pos)


        def _turn_on_off_edit_mode(self, view, button):
            if view.isInEditMode:
                view.isInEditMode = False
                button.image.set_alpha(50)
            else:
                view.isInEditMode = True
                button.image.set_alpha(255)

        def _create_remove_node(self, event, view, pos):
            if event.button == pygame.BUTTON_LEFT and view.isInEditMode:
                view.add_element(Node(pos[0], pos[1]))
            elif event.button == pygame.BUTTON_RIGHT and view.isInEditMode:
                view.remove_element(pos)

    def __init__(self, changer):
        super().__init__(changer)
        self.controllers = [self.ClickController()]
        editIcon = pygame.image.load('icons\\edit_icon.png').convert_alpha()
        editIcon.set_alpha(50)
        editButton = ImageButton(editIcon, screen.rect.width - 0.05 * screen.rect.width, 0, 50, 50)
        self.sprites.append(editButton)
        self.isInEditMode = False
        self.graphHistory = [Graph()]
        self.graphHistory[0].fill()
        self.pos = 0
        # self.add_start_elements()
        self.draw_graph()

    def add_element(self, element):
        self.graphHistory[self.pos].add_element(element)
        self.sprites.append(element)

    def remove_element(self, pos):
        clicked_sprites = [s for s in self.sprites if  not isinstance(s, FreeText) and s.rect.collidepoint(pos)]
        print(clicked_sprites)
        try:
            element = clicked_sprites[0]
            self.graphHistory[self.pos].remove_element(element)
            self.draw_graph()
        except IndexError:
            pass

    def run_controllers(self, event):
        for controller in self.controllers:
            controller(event, self)

    def draw_graph(self):
        print(self.pos)
        graph = self.graphHistory[self.pos]
        while len([s for s in self.sprites if isinstance(s, (Edge, Node))]) > 0:
            for sprite in self.sprites:
                if isinstance(sprite, (Edge, Node)):
                    self.sprites.remove(sprite)

        for node in graph.nodes:
            self.sprites.append(node)
        for edge in graph.edges:
            self.sprites.append(edge)
        self.draw_extra_info()

    def draw_extra_info(self):
        pass

    def fill_history(self, end: Node):
        pass

    def rewind_history(self):
        if self.pos > 0:
            self.pos -= 1
        self.draw_graph()

    def fast_forward_history(self):
        if self.pos < len(self.graphHistory) - 1:
            self.pos += 1
        self.draw_graph()

    def run_algorithm(self, graph: Graph):
        pass

    def draw_route(self, graph: Graph, end: Node):

        def find_node_index(node):
            for z in range(len(graph.nodes)):
                if graph.nodes[z] == node:
                    return z

        for node in graph.nodes:
            if node.start:
                start = node
                break
        else:
            print("Error brak startu")
            return

        for node in graph.nodes:
            node.selected = False

        start.selected = True
        end.selected = True

        currentNode = end
        previousNode = graph.nodes[graph.p[find_node_index(end)]]
        while currentNode is not start:
            for edge in previousNode.edges:
                if edge.node1 == currentNode or edge.node2 == currentNode:
                    edge.color = (255, 0, 0)
            currentNode = previousNode
            previousNode = graph.nodes[graph.p[find_node_index(previousNode)]]
