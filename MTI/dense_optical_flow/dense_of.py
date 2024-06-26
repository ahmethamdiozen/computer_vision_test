import numpy as np
import cv2

cap = cv2.VideoCapture("../video.mp4")
#cap = cv2.VideoCapture('../video1.mp4')

ret, frame1 = cap.read()
prvs = cv2.cv2tColor(frame1, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[: , 1] = 255

while(1):
    _, frame2 = cap.read()

    next = cv2.cv2tColor(frame2, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang*180/np.pi/2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    bgr = cv2.cv2tColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow("frame1", frame2)
    cv2.imshow('frame2', bgr)
    k = cv2.waitKey(30) & 0xff
    
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('dense_img.png', frame2)
        cv2.imwrite('dense_hsv.png', bgr)
    prvs = next

cap.release()
cv2.destroyAllWindows()