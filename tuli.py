import pyautogui
import time
time.sleep(3)
count=1
while count <=50:
    pyautogui.typewrite("I Love You Yeasin "+ str(count))
    pyautogui.press("enter")
    count = count+1