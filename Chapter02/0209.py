# 0209.py

import cv2, pafy
url = 'https://www.youtube.com/watch?v=S_0ikqqccJs'
video = pafy.new(url)
print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)

best = video.getbest(preftype = 'webm') # 'mp4', '3gp'
print('best.resolution', best.resolution)

cap = cv2.VideoCapture(best.url)
while(True):
    retval, frame = cap.read()
    if not retval:
        break
    cv2.imshow('frame', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow('edges', edges)
    
    key = cv2.WaitKey(25)
    if key == 27:
        break
cv2.destroyAllWindows()


