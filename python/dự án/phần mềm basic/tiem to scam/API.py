import pyautogui
import time

def click(x,y):
    y=797
    pyautogui.mouseDown()
    pyautogui.moveTo(x,y)


while True:
    pic =pyautogui.locateOnScreen("dota.png",region=(700,500,300,130),confidence=0.6)
    if pic !=None:
        #print(pyautogui.center(pic))
        #print(pyautogui.locateOnScreen("dota.png",confidence=0.5))

        x,y =pyautogui.center(pyautogui.locateOnScreen("dota.png",region=(700,600,300,430),confidence=0.2))
        pyautogui.mouseDown(x,767)

    


    else:
        print("i dont see")#254 167
       

