from M.Edge import Edge


class BasicView:
    def __init__(self, changer):
        self.sprites = []
        self.changer = changer

    def draw_elements(self):
        edges = [sprite for sprite in self.sprites if isinstance(sprite, Edge)]
        spritesWithoutEdges = [sprite for sprite in self.sprites if sprite not in edges]
        for edge in edges:
            edge.update()
            edge.draw(self.changer.surface)

        for element in spritesWithoutEdges:
            element.update()
            element.draw(self.changer.surface)

        # for sprite in self.sprites:
        #     sprite.update()
        #     sprite.draw(self.changer.surface)

    def run_controllers(self, event):
        pass
