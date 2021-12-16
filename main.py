import cv2
from collections import deque
frameWidth = 256
frameHeight = 144
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', frameWidth, frameHeight)
nseconds = 10
fps = 25
ring = deque(maxlen=fps * nseconds)
if not cap.isOpened():
    print("capture did not open!")
    exit(1)

while (True):
    success, img = cap.read()
    if not success:
        print("no frame")
        break

    ring.append(img)
    if len(ring)>=fps * nseconds:
        src = ring.popleft()
        cv2.imshow("image", src)
    k = cv2.waitKey(int(1000.0 / fps))
    if k == 27:
        break
