from M.Edge import Edge
from M.Node import Node

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
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
        edge7 = Edge(nodeE, nodeC)
        edge7.weight = 5
        self.edges.append(edge1)
        self.edges.append(edge2)
        self.edges.append(edge3)
        self.edges.append(edge4)
        self.edges.append(edge5)
        self.edges.append(edge6)
        self.edges.append(edge7)