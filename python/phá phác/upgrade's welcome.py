import pyautogui as py
import time
import keyboard
"""
while True: 
    x, y= py.position()
    print(x,y)
    time.sleep(0.5)#189 26
"""
a = 189
b =0

#500 455 - #4 455 vị trí set up web
py.moveTo(a, 26) #di chuyển ở đầu tab
py.click()
time.sleep(0.5)
py.moveTo(153,370)
time.sleep(2)
py.moveTo(a, 26)
while True:
    
    py.hotkey('ctrl','t')
    time.sleep(1)
    py.mouseDown(button='left')
    py.moveTo(a+(500-189),26,1) #379 -> phép toán lập 189+(379-189)
    py.mouseUp(button='left') 
    py.hotkey('ctrl','v')
    py.press('enter')
    py.moveTo(153,370)
    time.sleep(2)
    a+=505-189
    b+=1
    if b ==1:
        break
    py.moveTo(a+110,26)
#https://www.facebook.com/watch/?v=1230955987511938&extid=CL-UNK-UNK-UNK-AN_GK0T-GK1C&mibextid=l2pjGR&ref=sharing