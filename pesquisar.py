import pyautogui
from time import sleep


def pesquisar_my_repositorio():
    for x in range(7):
        pyautogui.press("tab")
    sleep(2)
    pyautogui.write("command_line")
    pyautogui.press("enter")