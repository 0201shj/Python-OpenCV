# 0202.py
import cv2

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile) # cv2.imread(imageFile, cv2.IMREAD_COLOR)
cv2.imwrite('./result/lena.bmp', img)
cv2.imwrite('./result/lena.png', img)
cv2.imwrite('./result/lena2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./result/lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])