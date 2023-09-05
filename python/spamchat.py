
from pyautogui import *
import time

limit = input('Enter your Limit: ')
msg = input('Enter Your Message: ')

i = 0

time.sleep(10)

while i< int(limit):
  
  typewrite(msg)
  press('Enter')

  i+=1 
 