from V.Views.GraphView import GraphView
from M.Edge import Edge
from M.Node import Node
from M.Graph import Graph
import copy


class DijkstraView(GraphView):
    def __init__(self, changer):
        super().__init__(changer)
        self.changer = changer


    def run_algorithm(self, graph: Graph):
        def min_value_index():
            index = 0
            val = 999999999999999999999
            for z in range(len(graph.d)):
                if graph.d[z] < val and graph.nodes[z].visited is not True:
                    index = z
                    val = graph.d[index]
            return index

        def find_node_index(n):
            for z in range(len(graph.nodes)):
                if graph.nodes[z] == n:
                    return z
            print("nie znaleziono wierzchołka")

        # https://eduinf.waw.pl/inf/alg/001_search/0138.php <----- HOW
        if len(graph.S) == 0:  # Przy pierwszej iteracji zainicjuj tablice p i d oraz znajdz poczatek i zanacz w d
            for node in graph.nodes:
                graph.p.append(-1)
                graph.d.append(9999999999999999)

            for x in range(0, len(graph.nodes)):
                if graph.nodes[x].start:
                    graph.d[x] = 0

        for node in graph.nodes:
            for edge in node.edges:
                edge.selected = False
            node.selected = False

        if len(graph.S) < len(graph.nodes):
            u = graph.nodes[min_value_index()] # aktualny wierzchołek
            graph.S.append(u)
            u.visited = True
            u.selected = True
            for w_edge in u.edges:
                w = w_edge.node1 if w_edge.node1 != u else w_edge.node2 # kolejny wierzchołek

                if w not in graph.S:
                    w_edge.selected = True
                    w_index = find_node_index(w)
                    u_index = find_node_index(u)
                    if graph.d[w_index] > graph.d[u_index] + w_edge.weight:
                        graph.d[w_index] = graph.d[u_index] + w_edge.weight
                        graph.p[w_index] = u_index

        return graph

    def fill_history(self):

        while len(self.graphHistory[-1].S) < len(self.graphHistory[0].nodes):
            print(len(self.graphHistory[0].nodes) - len(self.graphHistory[-1].S))
            self.graphHistory.append(self.run_algorithm(copy.copy(self.graphHistory[-1])))
            self.pos += 1
        self.graphHistory.append(copy.copy(self.graphHistory[-1]))
        self.pos += 1
        graph = self.graphHistory[-1]
        self.draw_route(graph, graph.nodes[-1])
        for node in self.graphHistory[-1].nodes:
            for edge in node.edges:
                edge.selected = False
