from github import pesquisar_github
from pesquisar import pesquisar_my_repositorio
from acessando_repository import acessando_repository
import pyautogui
from time import sleep

pyautogui.PAUSE = 0.7

def abrir_google_chrome():
    try:
        pyautogui.press("win")
        pyautogui.write("google_chrome")
        pyautogui.press("enter")
        sleep(1)
    except Exception as e:
        print(f"Erro ao abrir google chorme: {e}")

def main ():
    abrir_google_chrome()
    pesquisar_github()
    pesquisar_my_repositorio()
    acessando_repository()

if __name__ == "__main__":
    main()