import cv2

from PIL import Image

import numpy as np

def get_limits(color):
    # Gelen BGR rengi numpy uint8 formatına çeviriyoruz
    c = np.uint8([[color]])
    
    # BGR → HSV dönüşümü
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    
    # Hue (renk tonu) değerini alıyoruz
    hue = hsvC[0][0][0]
    
    # Alt ve üst HSV sınırlarını belirliyoruz
    lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
    upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    
    return lowerLimit, upperLimit


yellow = [0, 255, 255]
cam = cv2.VideoCapture(0) #harici kamera falan olursa kamera ıd'sini yazacaksın

while True:
    ret, frame = cam.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerimit, upperlimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerimit, upperlimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    print(bbox)
    
    cv2.imshow('frame',mask)
    
    if cv2.waitKey(40) & 0xFF == ord('q'): #imshow yap q diye kontrol de et
        break
    

cam.release()
cv2.destroyAllWindows()