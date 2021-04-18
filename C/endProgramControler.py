import pygame


def end_program_controller(event, program):
    if event.type == pygame.QUIT:
        program.exit_button_was_clicked = True