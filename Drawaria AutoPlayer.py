from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import pynput
import time
import random
import cv2
import numpy as np

# Configuración del WebDriver
chrome_driver_path = r'C:\SeleniumDrivers\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# URL de la página
url = 'https://drawaria.online/'
driver.get(url)

# Función para iniciar el juego
def start_game():
    # Esperar a que la página cargue
    time.sleep(5)

    # Ingresar el nombre del jugador
    player_name_input = driver.find_element(By.ID, 'playername')
    player_name_input.send_keys('AutoPlayer')

    # Hacer clic en el botón de jugar
    play_button = driver.find_element(By.ID, 'quickplay')
    play_button.click()

# Función para detectar la palabra a dibujar
def detect_word():
    # Aquí puedes implementar la lógica para detectar la palabra en la pantalla
    # Por ejemplo, puedes usar OpenCV para capturar la pantalla y detectar la palabra
    screenshot = pyautogui.screenshot(region=(100, 100, 300, 100))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(screenshot, (x, y), (x+w, y+h), (0, 255, 0), 2)
        pyautogui.click(x + 100, y + 50)
        break
    return "example"  # Aquí debes obtener la palabra a dibujar

# Función para dibujar automáticamente
def draw_automatically(word):
    # Aquí puedes implementar la lógica para dibujar la palabra
    # Por ejemplo, puedes usar pyautogui para mover el mouse y dibujar
    if word == "circle":
        pyautogui.moveTo(200, 200)
        pyautogui.dragTo(200, 300, duration=1)
        pyautogui.dragTo(300, 300, duration=1)
        pyautogui.dragTo(300, 200, duration=1)
        pyautogui.dragTo(200, 200, duration=1)
    elif word == "square":
        pyautogui.moveTo(200, 200)
        pyautogui.dragTo(300, 200, duration=1)
        pyautogui.dragTo(300, 300, duration=1)
        pyautogui.dragTo(200, 300, duration=1)
        pyautogui.dragTo(200, 200, duration=1)
    else:
        pyautogui.moveTo(random.randint(100, 500), random.randint(100, 500))
        pyautogui.dragTo(random.randint(100, 500), random.randint(100, 500), duration=1)

# Función para adivinar palabras
def guess_word():
    # Aquí puedes implementar la lógica para adivinar la palabra
    # Por ejemplo, puedes usar pynput para escribir palabras aleatorias
    keyboard = pynput.keyboard.Controller()
    keyboard.type('word')
    keyboard.press(Keys.ENTER)
    keyboard.release(Keys.ENTER)

# Función principal
def main():
    start_game()

    # Esperar a que el juego comience
    time.sleep(10)

    # Simular el juego
    while True:
        # Detectar la palabra a dibujar
        word = detect_word()

        # Dibujar automáticamente
        draw_automatically(word)

        # Adivinar palabras
        guess_word()

        # Esperar un tiempo antes de la siguiente iteración
        time.sleep(5)

        # Verificar si se presionó la tecla Esc para detener el script
        if pynput.keyboard.Controller().press(pynput.keyboard.Key.esc):
            break

if __name__ == '__main__':
    main()
5
