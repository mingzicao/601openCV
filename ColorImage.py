import cv2

img = cv2.imread('Lenna.png')

cv2.imshow("Original Image",img)

[b,g,r] = cv2.split(img) #RGB
cv2.imshow('B',b)
cv2.imwrite('B.png',b)
cv2.imshow('R',r) 
cv2.imwrite('R.png',r)
cv2.imshow('G',g)
cv2.imwrite('G.png',g)
RGB_part = img[20,25]
print("RGB part",RGB_part)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #HSV
[h,s,v] = cv2.split(hsv)
cv2.imshow('H',h)
cv2.imwrite('H.png',h)
cv2.imshow('S',s)
cv2.imwrite('S.png',s)
cv2.imshow('V',v)
cv2.imwrite('V.png',v)
hsv_part = hsv[20,25]
print("HSV part",hsv_part)

YCC = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB) #YCC
[y,Cb,Cr] = cv2.split(YCC) 
cv2.imshow('Y',y)
cv2.imwrite('Y.png',y)
cv2.imshow('Cb',Cb)
cv2.imwrite('Cb.png',Cb)
cv2.imshow('Cr',Cr)
cv2.imwrite('Cr.png',Cr)
YCC_part = YCC[20,25]
print("YCC part:", YCC_part)

cv2.waitKey(0)
