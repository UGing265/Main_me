import pyautogui
import time
import keyboard
import os


 
"""
while True:
    x,y = pyautogui.position()
    print(x,y)
    time.sleep(1)
    if keyboard.is_pressed('z'):
         break
"""
print('dota'*2)
b=0
a=0
c=0
time.sleep(5)
while True:
    pyautogui.hotkey('ctrl','t')
    if keyboard.is_pressed('F9'):
         break
    pyautogui.moveTo(170,50)
    pyautogui.click()
    if keyboard.is_pressed('F9'):
         break
    
    pyautogui.hotkey("ctrl","v")
    if keyboard.is_pressed('F9'):
         break
    
    
    pyautogui.press('enter')
    pyautogui.moveTo(510,416)
    time.sleep(7)
    if keyboard.is_pressed('F9'):
         break
  
    
    b+=1
    a+=1
    if a >= 5:
     pyautogui.moveTo(152,12)  
     pyautogui.click()
     time.sleep(1)
     pyautogui.hotkey('ctrl','w')
     time.sleep(1)
     pyautogui.hotkey('ctrl','w')
     c+=1
     a = 0
     if b >= 13:
               pyautogui.moveTo(152,12)  
               pyautogui.click()
               time.sleep(1)
               pyautogui.hotkey('ctrl','w')
               time.sleep(1)
               pyautogui.hotkey('ctrl','w')
               time.sleep(1)
               pyautogui.hotkey('ctrl','w')
          
               if b >= 100: 
                    pyautogui.hotkey('ctrl','w')
                    time.sleep(1)
                    pyautogui.hotkey('ctrl','w')
                    time.sleep(0.5)
                    pyautogui.hotkey('ctrl','w')
                    time.sleep(0.5)
                    
                    b=0
     if c == 500:
          os.system("shutdown /s /t 1")

 
               
"""
kham khảo
import os
import datetime
import time

# Đặt thời điểm cần shut down
shutdown_time = datetime.datetime(2023, 3, 22, 1, 0, 0) # Ngày 22/3/2023 lúc 1 giờ sáng

# Tính khoảng thời gian cần đợi
wait_time = (shutdown_time - datetime.datetime.now()).total_seconds()

# Đợi trong khoảng thời gian xác định
time.sleep(wait_time)

# Thực hiện lệnh shut down
os.system("shutdown /s /t 1")

"""
     
#https://www.facebook.com/watch/?v=1230955987511938&extid=CL-UNK-UNK-UNK-AN_GK0T-GK1C&mibextid=l2pjGR&ref=sharinghttps://www.facebook.com/watch/?v=1230955987511938&extid=CL-UNK-UNK-UNK-AN_GK0T-GK1C&mibextid=l2pjGR&ref=sharing
