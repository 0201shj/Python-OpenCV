# 0415.py
import cv2
src = cv2.imread('./data/lena.jpg')

dst1 = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)         #시계방향으로 90도 회전
dst2 = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)  #시계방향으로 270도 회전

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()