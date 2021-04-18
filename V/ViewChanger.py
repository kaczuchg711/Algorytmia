import pygame

from V.Views.StartView import StartView
from C.ClickControler import ClickController
from static import ScreenHeight, ScreenWith


class ViewChanger:

    def __init__(self):
        self.actualView = 0
        self.views = []
        self.views.append(StartView())
        self.exit_button_was_clicked = False
        self.clickController = ClickController()

    def display(self):
        pygame.init()

        size = [ScreenWith, ScreenHeight]
        surface = pygame.display.set_mode(size)

        while not self.exit_button_was_clicked:
            surface.fill((0, 0, 0))
            self._run_controlers()
            self.views[self.actualView].drawElements(surface)

            pygame.display.flip()

        pygame.quit()

    def end_program_controller(self, event):
        if event.type == pygame.QUIT:
            self.exit_button_was_clicked = True

    def change_view(self, newViewNumber):
        self.actualView = newViewNumber

    def _run_controlers(self):
        for event in pygame.event.get():
            self.end_program_controller(event)
            self.clickController(event, self.views[self.actualView].sprites, self.views[self.actualView])
