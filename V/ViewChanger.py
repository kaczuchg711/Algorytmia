import pygame

from M.Node import Node
from V.Views.StartView import StartView
from C.ClickControler import ClickController


class ViewChanger:

    def __init__(self):
        self.actualView = 0
        self.views = []
        self.views.append(StartView())
        self.exit_button_was_clicked = False
        self.clickControler = ClickController()

    def display(self):
        pygame.init()

        size = [900, 900]
        surface = pygame.display.set_mode(size)

        while not self.exit_button_was_clicked:
            surface.fill((0, 0, 0))
            self._run_controlers()
            self.views[self.actualView].drawElements(surface)

            pygame.display.flip()

        pygame.quit()

    def end_program_controler(self, event):

        if event.type == pygame.QUIT:
            self.exit_button_was_clicked = True

    def change_view(self, newViewNumber):
        self.actualView = newViewNumber


    def _run_controlers(self):
        for event in pygame.event.get():
            self.end_program_controler(event)
            self.clickControler(event, self.views[self.actualView].sprites,self.views[self.actualView])
