import cv2 
import numpy as np 
from scipy import ndimage as ndi
from scipy.ndimage.measurements import label

def largest_component(indices):
    #this function takes a list of indices denoting
    #the white regions of the image and returns the largest 
    #white object of connected indices 

    return_arr = np.zeros((512,512), dtype=np.uint8)
    for index in indeces:
        return_arr[index[0]][index[1]] = 255

    return return_arr

image = cv2.imread('sonar_dataset/useful/sonarXY_5.bmp', 0)
image_gaussian = ndi.gaussian_filter(image, 4)
image_gaussian_inv = cv2.bitwise_not(image_gaussian)
kernel = np.ones((3,3),np.uint8)

# double thresholding extracting the sides of the rectangle
ret1, img1 = cv2.threshold(image_gaussian_inv, 120, 255, cv2.THRESH_BINARY)
ret2, img2 = cv2.threshold(image_gaussian_inv, 150, 255, cv2.THRESH_BINARY)

double_threshold = img1 - img2
closing = cv2.morphologyEx(double_threshold, cv2.MORPH_CLOSE, kernel1)

labeled, ncomponents = label(closing, kernel)
indices = np.indices(closing.shape).T[:,:,[1, 0]]
twos = indices[labeled == 2]
area =[np.sum(labeled==val) for val in range(ncomponents+1)]

rectangle = largest_component(twos)

cv2.imshow('rectangle', rectangle)
cv2.waitKey(0)