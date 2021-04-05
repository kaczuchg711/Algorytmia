class BasicView:
    def __init__(self):
        self.sprites = []

    def drawElements(self, surface):
        for element in self.sprites:
            element.draw(surface)
            element.update()
