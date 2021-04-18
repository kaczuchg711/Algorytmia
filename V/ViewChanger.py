import pygame

from C.endProgramControler import end_program_controller
from V.Views.DijkstraView import DijkstraView
from V.Views.StartView import StartView
from static import ScreenHeight, ScreenWith


class ViewChanger:

    def __init__(self):
        self.actualView = 0
        self.views = []
        self.views.append(DijkstraView())
        self.exit_button_was_clicked = False

    def display(self):
        pygame.init()
        size = [ScreenWith, ScreenHeight]
        surface = pygame.display.set_mode(size)

        while not self.exit_button_was_clicked:
            surface.fill((0, 0, 0))
            self.handle_events()
            self.views[self.actualView].draw_elements(surface)
            pygame.display.flip()

        pygame.quit()

    def change_view(self, newViewNumber):
        self.actualView = newViewNumber

    def handle_events(self):
        for event in pygame.event.get():
            end_program_controller(event, self)
            self.views[self.actualView].run_controllers(event)
