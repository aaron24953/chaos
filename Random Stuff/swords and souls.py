import pyautogui
import numpy as np
import datetime
import keyboard
import time

# image = pyautogui.screenshot()
# print(image)
# # image = image.crop((50,50,500,500))  # crop image to box
# image = np.array(image)  # rgb array of pixels
# print(image[561][211])


def findWindow():
    while True:
        screen = pyautogui.screenshot()
        screen = np.array(screen)
        for i in range(len(screen)):
            for j in range(len(screen[i])):
                if screen[i][j][0] == 122 and screen[i][j][1] == 28 and screen[i][j][2] == 189:
                    print(f"s at: {j},{i}")
                    return (j, i)


def critical(s: tuple[int, int]):
    while True and not keyboard.is_pressed("esc"):
        clicked = False
        box = (s[0]+370, s[1]+250, s[0]+370+200, s[1]+250+200)
        screen = pyautogui.screenshot()
        screen = screen.crop(box)
        # screen.save("test.png")
        screen = np.array(screen)
        for row in screen:
            for pixel in row:
                if pixel[0] == 204 and pixel[1] == pixel[2] == 0 and not clicked:
                    pyautogui.click()
                    time.sleep(0.25)
                    clicked = True
                    break
            if clicked:
                break


def dodge(s: tuple[int, int]):
    while True and not keyboard.is_pressed("esc"):
        box = (s[0]+370, s[1]+250, s[0]+370+300, s[1]+250+200)
        screen = pyautogui.screenshot()
        screen = screen.crop(box)
        # screen.save("test.png")
        screen = np.array(screen)
        if screen[70][160][0] == 255 and screen[70][160][1] == 255 and screen[70][160][2] == 255:
            pyautogui.press("a")
        if screen[103][200][0] == 255 and screen[103][200][1] == 255 and screen[103][200][2] == 255:
            pyautogui.press("s")
        if screen[175][175][0] == 255 and screen[175][175][1] == 255 and screen[175][175][2] == 255:
            pyautogui.press("w")


def attack(s: tuple[int, int]):
    wt = datetime.datetime.now()
    st = datetime.datetime.now()
    dt = datetime.datetime.now()
    gt = datetime.datetime.now()
    delay = 150  # ms
    gdelay = 50
    while True and not keyboard.is_pressed("esc"):
        box = (s[0], s[1]+250, s[0]+300, s[1]+250+300)
        screen = pyautogui.screenshot()
        screen = screen.crop(box)
        # screen.save("test.png")
        screen = np.array(screen)
        row = screen[120]
        for pixel in row:
            if pixel[0] == 185 and pixel[1] == 38 and pixel[2] == 42 and datetime.datetime.now() > dt + datetime.timedelta(milliseconds=delay) and datetime.datetime.now() > gt + datetime.timedelta(milliseconds=gdelay):
                pyautogui.press("d")
                dt = datetime.datetime.now()
                gt = datetime.datetime.now()
                break
        row = screen[20]
        for pixel in row:
            if pixel[0] == 185 and pixel[1] == 38 and pixel[2] == 42 and datetime.datetime.now() > wt + datetime.timedelta(milliseconds=delay) and datetime.datetime.now() > gt + datetime.timedelta(milliseconds=gdelay):
                pyautogui.press("w")
                wt = datetime.datetime.now()
                gt = datetime.datetime.now()
                break
        row = screen[200]
        for pixel in row:
            if pixel[0] == 185 and pixel[1] == 38 and pixel[2] == 42 and datetime.datetime.now() > st + datetime.timedelta(milliseconds=delay) and datetime.datetime.now() > gt + datetime.timedelta(milliseconds=gdelay):
                pyautogui.press("s")
                st = datetime.datetime.now()
                gt = datetime.datetime.now()
                break
        # row = screen[120]
        # for pixel in row:
        #     if pixel[0] == 241 and pixel[1] == 192 and pixel[2] == 0:
        #         pyautogui.press("a")
        #         break


s = findWindow()
# critical(s)
# dodge(s)
attack(s)
