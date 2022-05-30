import pyautogui
import time

text = input('Enter Message : ')
many = int(input('Enter How Many Messages : '))

time.sleep(4)

for x in range(many):
	pyautogui.write((text), interval=0.05)
	pyautogui.press('enter')
