import pyautogui
import time

print("░██████╗░██╗░░░██╗███████╗██████╗░██╗░░░██╗")
print("██╔════╝░╚██╗░██╔╝╚════██║██╔══██╗╚██╗░██╔╝")
print("██║░░██╗░░╚████╔╝░░░███╔═╝██████╦╝░╚████╔╝░")
print("██║░░╚██╗░░╚██╔╝░░██╔══╝░░██╔══██╗░░╚██╔╝░░")
print("╚██████╔╝░░░██║░░░███████╗██████╦╝░░░██║░░░")
print("░╚═════╝░░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░")
print("")
print("Spammer Messages 0.1 By Gyzby")
print("")
text = input('Enter Message : ')
print("")
many = int(input('Enter How Many Messages : '))
print("")
print("Wait 4s to start Spam")

time.sleep(4)

for x in range(many):
	pyautogui.write((text), interval=0.05)
	pyautogui.press('enter')
