# 0201.py
import cv2

imageFile = './data/lena.jpg'

img = cv2.imread(imageFile)  #cv2.IMREAD_COLOR
img2 = cv2.imread(imageFile, 0) #cv2.IMREAD_GRAYSCALE

cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img2)

height, width, channel = img.shape
print(height, width, channel)  #img.shape(512,512,3)
height2, width2 = img2.shape
print(height2, width2)  #img2.shape(512,512)

cv2.waitKey()
cv2.destroyAllWindows()

