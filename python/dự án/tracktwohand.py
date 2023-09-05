from cvzone.HandTrackingModule import HandDetector
import cv2
import pyautogui as py
import time
import numpy as np
"""
muốn kết nối obs = videocapture ?
cài plugin về https://github.com/Fenrirthviti/obs-virtual-cam/releases
bật obs lên chỉnh tool -> script -> python setting -> browse -> tìm chỗ folder có file chứa .py sau đó "select folder"
chuyển qua scrpit -> nhập file url-test.py
xong tool -> virtual cam -> chạy (start) 
thành công rồi chúc may mắn 
"""

wcam, hcam= 640,480
smooth = 5

plocx, plocy = 0,0
clocx,clocy =0,0

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

dec = HandDetector(detectionCon=0.8,maxHands=2)
screen_we,screen_hi = py.size() #1366 768
while True:
    _,img = cap.read()
    hands,img= dec.findHands(img, flipType=False)
    #hands= dec.findHands(img, draw=false)
    img_we, img_h,_ = img.shape #print(img_we,img_h)
    
    
    
    
    
    
    if hands:
        hand1=hands[0]
        lmList1=hand1["lmList"]#List of 21 Landmark points
        bbox1=hand1["bbox"]  #Bounding box info x,y,w,h
        centerPoint1 = hand1["center"]#center ò the hand cx,cv
        handType1 = hand1["type"]#hand type left of right
        #rint(lmList1[8])
        print(len(lmList1[8]),lmList1[8] )#demo landmark
        if len(lmList1)!=0:
            x1,y1,_=lmList1[8] # dùng dấu * này để chứa giá trị còn lại vì khi khai báo a b = [2,3,4] sẽ báo lỗi too many vì dư thằng 4 ở ngoài nên gây lỗi
            x2,y2,*other=lmList1[12]
            print(x1,y1)
         
        finger1 = dec.fingersUp(hand1)
        cv2.rectangle(img,(100,100),(wcam-100,hcam-100),(30,30,255),2)
        if finger1[1] == 1 and finger1[2]==0:
            print("ok tốt")
            x3 = np.interp(x1,(100,wcam-100),(0,screen_we))
            y3 = np.interp(y1,(100,hcam-100),(0,screen_hi))

            #smoothen VAlues
            clocx = plocx +(x3 - plocx)/smooth
            clocy = plocy +(y3 - plocy)/smooth
            print(x3,y3)
            py.moveTo( x3, y3)
            cv2.circle(img,(x1,y1),15,(30,255,255),cv2.FILLED)#img, vị trí, radius, màu, kiểu hình
        #a = py.moveTo(size)
        if finger1[1] == 1 and finger1[2] == 1 and finger1[3] == 0 and finger1[4] == 0:
           # length, img, _ = dec.findDistance(8,12,img)
            py.click()
            time.sleep(0.2)
            print("TRIGGER")
          

        print(finger1)
        if len(hands)==2:
            hand2=hands[1]
            lmList2=hand2["lmList"]#List of 21 Landmark points
            bbox2=hand2["bbox"]  #Bounding box info x,y,w,h
            centerPoint2 = hand2["center"]#center ò the hand cx,cv
            handType2 = hand2["type"]#hand type left of right
            
            finger2 =dec.fingersUp(hand2)#dò ngón tay xem mở hay tắt return 0 1
            print(finger1,finger2)
            if (finger2[0] ==1 and finger2[1] == 0 and finger2[2] == 0 and 
            finger2[3] ==0 and finger2[4] ==0 and finger2[0] ==1 and finger1[1] == 0 
            and finger1[2] == 0 and finger1[3] ==0 and finger1[4] ==0):
                py.hotkey("win","d")
                time.sleep(5)

    cv2.imshow("dota",img)
    cv2.waitKey(1)