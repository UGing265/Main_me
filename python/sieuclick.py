import pyautogui as py
import time

py.FAILSAFE = False

time.sleep(3)
print(py.position())
print(py.size())
print(py.onScreen(1919, 600))
#py.moveTo(0, 0,2)

##py.moveTo(200,200,2)

#py.moveTo(960,540,5)


py.click(732, 602, 1000, 0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001, 'left')
