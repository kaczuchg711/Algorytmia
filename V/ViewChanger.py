import pygame

from C.endProgramControler import end_program_controller
from V.Views.DijkstraView import DijkstraView
from V.Views.StartView import StartView
from static import screen


class ViewChanger:
    def __init__(self):
        self.views = {"StartView": StartView(self)}
        self.actualView = self.views["StartView"]
        self.exit_button_was_clicked = False
        size = [screen.rect.width, screen.rect.height]
        self.surface = pygame.display.set_mode(size)

    def display(self):
        pygame.init()
        size = [screen.rect.width, screen.rect.height]
        surface = pygame.display.set_mode(size)

        while not self.exit_button_was_clicked:
            surface.fill((0, 0, 0))
            self.handle_events()
            self.actualView.draw_elements()
            pygame.display.flip()

        pygame.quit()

    def change_view(self, viewName):
        self.actualView = self.views[viewName]

    def handle_events(self):
        for event in pygame.event.get():
            end_program_controller(event, self)
            self.actualView.run_controllers(event)
