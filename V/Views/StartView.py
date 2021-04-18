from M.Button import Button
from V.Views.BasicView import BasicView


class StartView(BasicView):

    def __init__(self):
        super().__init__()
        self.sprites = [Button("siema",10, 10, 100, 100)]

    def draw_elements(self, surface):
        for element in self.sprites:
            element.draw(surface)
            element.update()
