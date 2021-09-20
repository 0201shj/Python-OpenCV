#0806.py
import cv2
import numpy as np

#1
src = cv2.imread('./data/CornerTest.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

K = 5
corners = cv2.goodFeaturesToTrack(gray, maxCorners=K, qualityLevel= 0.05, minDistance= 10)

print('corners.shape = ', corners.shape)
print('corners = ', corners)

#2
K2 = 10
corners2 = cv2.goodFeaturesToTrack(gray, maxCorners= K2, qualityLevel= 0.05, minDistance= 10, useHarrisDetector= True, k = 0.04)
print('corners2.shape = ', corners2.shape)
print('corners2 = ', corners2)

#3
dst = src.copy()
corners = corners.reshape(-1, 2)
for x, y in corners:
    cv2.circle(dst, (x, y), 5, (0,0,255), -1)

dst2 = src.copy()
corners2 = corners2.reshape(-1, 2)
for x, y in corners2:
    cv2.circle(dst2, (x, y), 5, (255, 0, 0), 2)

cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()