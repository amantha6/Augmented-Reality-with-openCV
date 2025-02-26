import cv2
import numpy as np
#getting the input image
#resize the image to make the algorithm run faster
input_image = cv2.imread('pikachu.png')
input_image=cv2.resize(input_image,(400,550),interpolation=cv2.INTER_AREA)
#converting to gray image, feature detection is based on grayscale images
gray_image=cv2.cvtColor(input_image,cv2.COLOR_BGR2GRAY)

#Initiate ORB object
#Creates an ORB object with the parameter nfeatures=1000, which limits detection to the 1000 strongest features
orb=cv2.ORB_create(nfeatures=1000)
#find the keypoints with ORB
#it has three methods, detect, compute and detectAndCompute
#Keypoints are distinctive points in the image (corners, edges, etc.)
# Descriptors are numerical representations of the area around each keypoint
keypoints, descriptors=orb.detectAndCompute(gray_image,None)
#drawing the keypoints on the image
final_keypoints=cv2.drawKeypoints(gray_image,keypoints,input_image,(0,255,0))
cv2.imshow('ORB Keypoints',final_keypoints)
cv2.waitKey()
