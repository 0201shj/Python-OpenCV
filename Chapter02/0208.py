# 0208.py
import cv2

cap = cv2.VideoCapture('http://192.168.0.3:4747/mjpegfeed')
#cap = cv2.VideoCapture('http://192.168.0.3:4747/mjpegfeed?640x480')
#cap = cv2.VideoCapture('http://192.168.0.3:4343/video') # IP Webcam

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print('frame_size =',frame_size)

while True:
    retval, frame = cap.read()
    if not retval:
        break
    cv2.imshow('frame', frame)

    key = cv2.waitKey(25)
    if key == 27:
        break
if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()