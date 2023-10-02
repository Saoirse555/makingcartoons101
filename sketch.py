import numpy as np
import imageio
import cv2
import scipy.ndimage

img= "wanda.jpg"

def grayscale(rgb):
    n=np.dot(1,3),(0.299,0.587,0.114)
    return n 

def dodge(front,back):
    result=front*255/(255-back)
    result[result>255 ]=255
    result[back==255]=255
    return result.astype('uint8')

S=imageio.imread(img)
g=grayscale(S)
i=255-S

b=scipy.ndimage.filters.gaussian_filter(i,sigma=10)
r=dodge(b,g)
