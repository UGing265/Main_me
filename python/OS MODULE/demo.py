import os
import time
os.chdir('E:\\CC+\\python\\OS MODULE\\') #change dir

os.makedirs('gay/dota/sisi/') #useful -> creade folder ->2 -> 3 ->...
#os.mkdir('scam/sisi') #no use this beacause 'scam folder' didnt exit so we cant create folder 2 




print(os.listdir()) #print dir here
time.sleep(2)

#same mk
os.removedirs('gay/dota/sisi/') #remove HAHA (ALL)
#os.rmdir('gay/dota/sisi/') # it will remove things i need to do
time.sleep(1)

os.rename("TEST.txt","RIP CLICK ME.txt")
time.sleep(2)
os.rename("RIP CLICK ME.txt","TEST.txt")
time.sleep(2)

print(os.stat('YO.txt')) #u can copy texts at terminal and . paste here example print(os.stat('YO.txt').st_ino)