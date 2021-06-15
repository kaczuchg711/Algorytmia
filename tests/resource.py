import time
import pyautogui


def click_element(element):
    wait_until_element_is_visible(element)
    x, y = pyautogui.locateCenterOnScreen(element, confidence=.8)
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)


def wait_until_element_is_visible(image: str, waitTime=5):
    t = time.time()
    x = None
    while x is None:
        x = pyautogui.locateCenterOnScreen(image, confidence=.8)
        if time.time() - t > waitTime:
            raise TimeoutError("element not visible since 5s")


def scroll_until_element_is_visible(images, direction=-1):
    x = None

    while x is None:
        for image in images:
            x = pyautogui.locateCenterOnScreen(image, confidence=.8)
            if x is not None:
                element = image
                break
        pyautogui.scroll(100 * direction)

    return element


def pageDown_until_element_is_visible(images):
    x = None

    while x is None:
        for image in images:
            x = pyautogui.locateCenterOnScreen(image, confidence=.8)
            if x is not None:
                element = image
                break
            pyautogui.press("num3")
            pyautogui.press("numlock")
            pyautogui.press("num3")
            pyautogui.press("numlock")

    return element


def open_right_click_mouse_menu():
    x, y = pyautogui.size()
    pyautogui.rightClick(x / 2, 0)


def click_element_in_right_click_mouse_menu(element):
    open_right_click_mouse_menu()
    wait_until_element_is_visible(element)
    x, y = pyautogui.locateCenterOnScreen('displaySettings.jpg', confidence=.9)
    pyautogui.click(x, y)
