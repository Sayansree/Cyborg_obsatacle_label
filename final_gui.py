
import cv2
import os
import numpy as np

coordinates_list = []
windowName = 'Drawing'
ctr =3904
low=np.array([0,0,0])
high=np.array([0,255,255])
def draw_circle(event, x, y, flags, param):
    
    

    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates_list.append([x,y])
        cv2.circle(img, (x, y), 2, (255, 0, ), -1)
        
        cv2.imshow(windowName, img)
def r():
    blur=cv2.GaussianBlur(img,(11,11),0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    low=np.array([0,129,102])
    high=np.array([15,238,243])
    mask=cv2.inRange(hsv,low,high)|cv2.inRange(hsv,np.array([175,100,95]),np.array([180,245,235]))
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    kernel = np.ones((11,11),np.uint8)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("th", closing)
    cv2.imwrite("auto\\frame_0"+ str(ctr)+ ".png",closing)
    cv2.waitKey(10)
def H(val):
    high[0]=val
    print(H)
    r()
def S(val):
    high[1]=val
    r()
def V(val):
    high[2]=val
    r()
def h(val):
    low[0]=val
    r()
def s(val):
    low[1]=val
    r()
def v(val):
    low[2]=val
    r()

def image_process( blank_image): 
    
    while(True):
        global ctr
        cv2.setMouseCallback(windowName, draw_circle)

        
        k = cv2.waitKey(20) & 0xFF
        if k == ord('a'):
            ctr-=2;
            break
        if k == ord('n'):
            break
        elif k == ord('s'):
            ctr = np.array(coordinates_list).reshape((-1,1,2)).astype(np.int32)
            cv2.drawContours(blank_image,[ctr],0,(255,255,255),-1)
            cv2.drawContours(img,[ctr],0,(255,255,255),-1)
            del coordinates_list[:]
            cv2.imshow(windowName, img)
            

        elif k == ord('d'):
            print(coordinates_list)
            cv2.imwrite("manual\\frame_0"+ str(ctr)+ ".png",blank_image)
            
            
            
    

cv2.namedWindow(windowName , cv2.WINDOW_NORMAL)
cv2.namedWindow("th" , cv2.WINDOW_NORMAL)
##cv2.createTrackbar("Hmin", "th" , 0, 180, h)
##cv2.createTrackbar("Smin", "th" , 0, 255, s)
##cv2.createTrackbar("Vmin", "th" , 0, 255, v)
##cv2.createTrackbar("Hmax", "th" , 0, 180, H)
##cv2.createTrackbar("Smax", "th" , 0, 255, S)
##cv2.createTrackbar("Vmax", "th" , 0, 255, V)
while ctr<4060:
    img=cv2.imread("img\\frame_0" + str(ctr)+ ".png")
    cv2.putText(img,"frame "+str(ctr),(0,15),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),1,cv2.LINE_AA)
    cv2.imshow(windowName, img)
    r() 
    blank_image = np.zeros(shape=img.shape, dtype=np.uint8)
    ##image_process( blank_image)
    ctr=ctr+1;


cv2.destroyAllWindows()
