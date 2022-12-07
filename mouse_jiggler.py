import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE = True


def moveInABox(speed, coordinates):
    duration = speed**-1
    for coordinate in coordinates:
        time.sleep(duration)
        pyautogui.moveTo(coordinate[0], coordinate[1], duration=duration)
    print("Cycle made at {}".format(datetime.now().time()))


LENGTH = 1440
HEIGHT = 900
GAP = 10

while True:
    moveInABox(speed=4, coordinates=[(GAP, GAP), (LENGTH - GAP, GAP), (LENGTH - GAP, HEIGHT - GAP), (GAP, HEIGHT - GAP)])