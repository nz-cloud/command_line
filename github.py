import pyautogui
from time import sleep

def pesquisar_github():
    pyautogui.write("github.com/nz-cloud")
    pyautogui.press("enter")
    sleep(2)