#0807.py
import cv2
import numpy as np

#1
src = cv2.imread('./data/chessBoard.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
patternSize 