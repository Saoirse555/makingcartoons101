#import libraries 
import cv2
import matplotlib
import numpy as np
#reading image
img=cv2.imread("wanda.jpg")
img1=cv2.imread("dog.jpg")
#to see how many pixels are in it 
px = img[100,100]
print( px )
#lets find the shape 
print(img.shape)
#lets find the size
print(img.size)
#values with less color
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
#rotating
# image = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) 
# cv2.imshow("Rotated",image)
#draw a circle
# cv2.circle(img,(80,80), 55, (255,0,0), -1)  
# cv2.imshow('image',img) 
#text on an image
#cv2.putText(img,'Dog',(10,500), font,1,(255,255,255),2) 
#blur
cv2.imshow('cv2.blur output', cv2.blur(img, (3,3))) 
#edges
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray =cv2.medianBlur(gray,5)
edges=cv2.adaptiveThreshold(gray, 255,
cv2.ADAPTIVE_THRESH_MEAN_C,
cv2.THRESH_BINARY,9,9)
#Make cartoon
color=cv2.bilateralFilter(img,9,250,250)
cartoon=cv2.bitwise_and(color,color,mask=edges)

cv2.imshow("Image",img)
cv2.imshow("Edges",edges)
cv2.imshow("Cartoon",cartoon)
cv2.imshow("Car",b)
cv2.imshow("Cart",g)
cv2.imshow("Carto",r)
cv2.waitKey(0)
#drawing 
mouse_events = [j for j in dir(cv2) if 'EVENT' in j]  
print(mouse_events)
# Creating mouse callback function  
def draw_circle(event,x,y,flags,param):  
    if(event == cv2.EVENT_LBUTTONDBLCLK):  
            cv2.circle(img,(x,y),50,(123,125, 200),-1)  
# Creating a black image, a window and bind the function to window  
img = np.zeros((512,512,3), np.uint8)  
cv2.namedWindow('image')  
cv2.setMouseCallback('image',draw_circle)  
while(1):  
    cv2.imshow('image',img)  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows() 