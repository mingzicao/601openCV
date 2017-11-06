import cv2
import numpy as np

src = cv2.imread("Lenna.png")
gray = cv2.cvtColor(src,cv2.COLOR_RGB2GRAY) 
#  0: Binary,      1: Binary Inverted,      2: Threshold Truncated,      
#  3: Threshold to Zero,      4: Threshold to Zero Inverted  
threshold_type = 2  
threshold_value = 128 
T, Thresholded = cv2.threshold(gray, threshold_value, 255, threshold_type )
cv2.imwrite("Thresholded_Image.png", Thresholded)


current_threshold = 128
max_threshold = 255
# Binary 
T, Binary_Threshold = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY);
cv2.imwrite("Binary_threshold.png", Binary_Threshold)

# Band 
threshold1 = 27
threshold2 = 125
T, lower = cv2.threshold(gray, threshold1, max_threshold,cv2.THRESH_BINARY)
T, upper = cv2.threshold(gray, threshold2, max_threshold,cv2.THRESH_BINARY_INV)
Band_Thresholding = cv2.bitwise_and(lower,upper)
cv2.imwrite("Band_thresholding.png",Band_Thresholding)

# Semi
T,thres = cv2.threshold(gray,current_threshold, max_threshold, cv2.THRESH_BINARY_INV or cv2.THRESH_OTSU);
Semi_Thresholding = cv2.bitwise_and(gray,thres);
cv2.imwrite("Semi_thresholding.png",Semi_Thresholding)

# Adaptive
Adaptive_Threshold = cv2.adaptiveThreshold(gray, max_threshold, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10 );
cv2.imwrite("Adaptive_Threshold.png",Adaptive_Threshold)

