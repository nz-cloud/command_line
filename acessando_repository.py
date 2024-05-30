import pyautogui
from time import sleep

def acessando_repository():
    for x in range (4):
        pyautogui.press("tab")
        sleep(1)
    pyautogui.press("enter")