class BasicView:
    def __init__(self):
        self.sprites = []

    def drawElements(self, surface):
        for element in self.sprites:
            element.update()
            element.draw(surface)

    def run_controllers(self, event):
        pass