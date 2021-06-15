import os

import threading
from time import sleep

import pyautogui


def run_program():
    os.system('python main.py')

from tests.resource import click_element

def first():
    x = threading.Thread(target=run_program)
    x.start()

    print("siema")

    click_element("tests/Dijkstra_button.png")
    click_element("tests/edit_button.png")


    pyautogui.moveTo(300, 300)
    pyautogui.click()
    pyautogui.moveTo(300, 600)
    pyautogui.click()
    pyautogui.moveTo(300, 300)
    pyautogui.click()
    pyautogui.moveTo(300, 600)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.keyDown("2")
    pyautogui.sleep(0.1)
    pyautogui.keyUp("2")
    pyautogui.keyDown("enter")
    pyautogui.sleep(0.1)
    pyautogui.keyUp("enter")
