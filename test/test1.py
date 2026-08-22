import pyautogui
import time

time.sleep(2)

pyautogui.moveTo(450, 300)

pyautogui.mouseDown()

pyautogui.moveTo(500, 400, duration=0.3)
pyautogui.moveTo(550, 300, duration=0.3)

pyautogui.mouseUp()

print("V COMPLETE")