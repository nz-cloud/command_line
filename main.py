from github import pesquisar_github
from pesquisar import pesquisar_my_repositorio
import pyautogui
from time import sleep

pyautogui.PAUSE = 0.5

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

if __name__ == "__main__":
    main()