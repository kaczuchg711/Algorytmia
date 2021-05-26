import copy
from time import sleep

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

        def __call__(self, event, view):

            if view.isInEditMode:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and view.isInEditMode:
                    for node in view.graphHistory[view.pos].nodes:
                        if node.rect.collidepoint(event.pos):
                            if node not in self.selectedNodes and len(self.selectedNodes) < 2:
                                node.selected = True
                                self.selectedNodes.append(node)

                            if len(self.selectedNodes) == 2:
                                # todo sometimes the program doesn't print this text
                                self.InputNumberText = FreeText("Input edge weight and press Enter", 24,
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
                        view.fill_history()
                        view.draw_graph()
                        #view.draw_route(view.graph, view.graph.nodes[0], view.graph.nodes[2])
                    elif event.key == pygame.K_LEFT:
                        view.rewind_history()
                    elif event.key == pygame.K_RIGHT:
                        view.fast_forward_history()

            if event.type == pygame.MOUSEBUTTONDOWN and len(self.selectedNodes) == 0:
                pos = pygame.mouse.get_pos()
                buttons = [button for button in view.sprites if isinstance(button, ImageButton)]

                for button in buttons:
                    if button.rect.collidepoint(event.pos) and event.button == 1:
                        self._turn_on_off_edit_mode(view, button)
                        break
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
            if event.button == pygame.BUTTON_LEFT and view.isInEditMode:
                view.add_element(Node(pos[0], pos[1]))
            elif event.button == pygame.BUTTON_RIGHT and view.isInEditMode:
                view.remove_element(pos)

    def __init__(self, changer):
        super().__init__(changer)
        self.controllers = [self.ClickController()]
        editIcon = pygame.image.load('icons\edit_icon.png').convert_alpha()
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
        clicked_sprites = [s for s in self.sprites if s.rect.collidepoint(pos)]
        try:
            self.sprites.remove(clicked_sprites[-1])
        except(IndexError):
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

    def fill_history(self):

        while len(self.graphHistory[-1].S) < len(self.graphHistory[0].nodes):
            print(len(self.graphHistory[0].nodes) - len(self.graphHistory[-1].S))
            self.graphHistory.append(self.run_algorithm(copy.copy(self.graphHistory[-1])))
            self.pos += 1
        self.graphHistory.append(copy.copy(self.graphHistory[-1]))
        self.pos += 1
        graph = self.graphHistory[-1]
        self.draw_route(graph,graph.nodes[0], graph.nodes[-1])
        for node in self.graphHistory[-1].nodes:
            for edge in node.edges:
                edge.selected = False

    def rewind_history(self):
        if self.pos > 0:
            self.pos -= 1
        self.draw_graph()

    def fast_forward_history(self):
        if self.pos < len(self.graphHistory) - 1:
            self.pos += 1
        self.draw_graph()

    def run_algorithm(self, graph: Graph):
        def min_value_index():
            index = 0
            val = 999999999999999999999
            for z in range(len(graph.d)):
                if graph.d[z] < val and graph.nodes[z].visited is not True:
                    index = z
                    val = graph.d[index]
            return index

        def find_node_index(node):
            for z in range(len(graph.nodes)):
                if graph.nodes[z] == node:
                    return z
            print("nie znaleziono wierzchołka")

        # https://eduinf.waw.pl/inf/alg/001_search/0138.php <----- HOW
        if len(graph.S) == 0:
            for node in graph.nodes:
                graph.p.append(-1)
                graph.d.append(9999999999999999)

            for x in range(0, len(graph.nodes)):
                if graph.nodes[x].start == True:
                    graph.d[x] = 0

        for node in graph.nodes:
            for edge in node.edges:
                edge.selected = False

        if len(graph.S) < len(graph.nodes):
            u = graph.nodes[min_value_index()]
            graph.S.append(u)
            u.visited = True
            for w_edge in u.edges:
                w = w_edge.node1 if w_edge.node1 != u else w_edge.node2

                if w not in graph.S:
                    w_edge.selected = True
                    w_index = find_node_index(w)
                    u_index = find_node_index(u)
                    if graph.d[w_index] > graph.d[u_index] + w_edge.weight:
                        graph.d[w_index] = graph.d[u_index] + w_edge.weight
                        graph.p[w_index] = u_index

        return graph




    def draw_route(self, graph: Graph, start: Node, end: Node):
        def find_node_index(node):
            for z in range(len(graph.nodes)):
                if graph.nodes[z] == node:
                    return z

        currentNode = end
        previousNode = graph.nodes[graph.p[find_node_index(end)]]
        while currentNode is not start:
            for edge in previousNode.edges:
                if edge.node1 == currentNode or edge.node2 == currentNode:
                    edge.color = (255, 0, 0)
            currentNode = previousNode
            previousNode = graph.nodes[graph.p[find_node_index(previousNode)]]
