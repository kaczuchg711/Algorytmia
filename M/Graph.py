import copy

import random

from M.Edge import Edge
from M.Node import Node


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.S = []
        self.d = []
        self.p = []

    def __copy__(self):
        self.nodes.sort()
        new = type(self)()
        new.d = copy.deepcopy(self.d)
        new.p = copy.deepcopy(self.p)
        for edge in self.edges:
            node1 = copy.copy(edge.node1)
            node2 = copy.copy(edge.node2)

            for node in new.nodes:
                if node.myEq(node1):
                    node1 = node
                    break
            else:
                new.nodes.append(node1)

            for node in new.nodes:
                if node.myEq(node2):
                    node2 = node
                    break
            else:
                new.nodes.append(node2)

            if edge.node1 in self.S:
                for node in new.S:
                    if node.myEq(node1):
                        break
                else:
                    new.S.append(node1)

            if edge.node2 in self.S:
                for node in new.S:
                    if node.myEq(node2):
                        break
                else:
                    new.S.append(node2)

            new_edge = Edge(node1, node2)
            new_edge.weight = edge.weight
            new_edge.selected = edge.selected
            new.edges.append(new_edge)

        new.nodes.sort()
        return new

    def add_element(self, element):
        if type(element) is Edge:
            self.edges.append(element)
            print("edge")
        elif type(element) is Node:
            self.nodes.append(element)
            print("node")

    def remove_element(self, element):
        if type(element) is Edge:
            print("Del edge")
            self.edges.remove(element)
            try:
                element.node1.edges.remove(element)
                element.node2.edges.remove(element)
            except ValueError:
                pass
            del element
        elif type(element) is Node:
            print("Del node")
            while len(element.edges):
                self.remove_element(element.edges[0])
            element.edges.clear()
            self.nodes.remove(element)
            del element

    def fill(self):
        x = random.randint(0, 5)
        # self.o1()
        self.o2()
        # self.o3()

    def o1(self):
        nodeA = Node(440, 300)
        nodeB = Node(750, 300)
        nodeC = Node(900, 400)
        nodeD = Node(440, 500)
        nodeE = Node(750, 500)
        self.nodes.append(nodeA)
        self.nodes.append(nodeB)
        self.nodes.append(nodeC)
        self.nodes.append(nodeD)
        self.nodes.append(nodeE)
        edge1 = Edge(nodeA, nodeB)
        edge1.weight = 6
        edge2 = Edge(nodeB, nodeC)
        edge2.weight = 5
        edge3 = Edge(nodeA, nodeD)
        edge3.weight = 1
        edge4 = Edge(nodeB, nodeE)
        edge4.weight = 2
        edge5 = Edge(nodeD, nodeE)
        edge5.weight = 1
        edge6 = Edge(nodeE, nodeC)
        edge6.weight = 5
        edge7 = Edge(nodeB, nodeD)
        edge7.weight = 2
        self.edges.append(edge1)
        self.edges.append(edge2)
        self.edges.append(edge3)
        self.edges.append(edge4)
        self.edges.append(edge5)
        self.edges.append(edge6)
        self.edges.append(edge7)

    def o2(self):

        nodeA = Node(400, 400)
        nodeB = Node(800, 400)
        nodeC = Node(1200, 400)
        nodeD = Node(800, 600)
        nodeE = Node(800, 200)
        nodeF = Node(600, 300)
        nodeG = Node(1000, 500)
        self.nodes.append(nodeA)
        self.nodes.append(nodeB)
        self.nodes.append(nodeC)
        self.nodes.append(nodeD)
        self.nodes.append(nodeE)
        self.nodes.append(nodeF)
        self.nodes.append(nodeG)
        edge1 = Edge(nodeA, nodeB)
        edge1.weight = 6
        edge2 = Edge(nodeB, nodeC)
        edge2.weight = 5
        edge3 = Edge(nodeA, nodeD)
        edge3.weight = 1
        edge4 = Edge(nodeB, nodeE)
        edge4.weight = 2
        edge5 = Edge(nodeD, nodeE)
        edge5.weight = 1
        edge6 = Edge(nodeE, nodeC)
        edge6.weight = 5
        edge8 = Edge(nodeA, nodeF)
        edge8.weight = 2
        edge9 = Edge(nodeF, nodeE)
        edge9.weight = 4
        edge10 = Edge(nodeA, nodeF)
        edge10.weight = 6
        edge11 = Edge(nodeF, nodeE)
        edge11.weight = 1
        edge12 = Edge(nodeD, nodeG)
        edge12.weight = 5
        edge13 = Edge(nodeG, nodeC)
        edge13.weight = 10

        self.edges.append(edge1)
        self.edges.append(edge2)
        self.edges.append(edge3)
        self.edges.append(edge4)
        self.edges.append(edge5)
        self.edges.append(edge6)
        self.edges.append(edge7)
        self.edges.append(edge8)
        self.edges.append(edge9)
        self.edges.append(edge10)
        self.edges.append(edge11)
        self.edges.append(edge12)
        self.edges.append(edge13)
