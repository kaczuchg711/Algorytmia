from V.Views.GraphView import GraphView


class DijkstraView(GraphView):
    pass

    def __init__(self, changer):
        super().__init__(changer)
        self.changer = changer