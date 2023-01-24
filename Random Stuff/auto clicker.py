# auto clicker

import keyboard
import pyautogui

while True:
    if keyboard.is_pressed("p"):
        for i in range(100):
            pyautogui.click()
