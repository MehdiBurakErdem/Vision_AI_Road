import cv2

img = cv2.imread("Photos/Photo3.png")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #Tek kanallı olması gerekiyor bunun çalışması için bu yuzden gray yaptık threshden once
#contours -> bu bir list(objenin sınır noktaları var).
for cnt in contours:
    if cv2.contourArea(cnt) > 100: #O contour’un kapladığı alanı hesaplar. noise de silmmek için > 100 diyebiliriz
        cv2.drawContours(img, cnt, -1, (0, 0, 255), 1) #görselden bakabilirsin daha sağlıklı kırmzı noktalar (B,G,R) -> (0,0,255)

        x1, y1, w, h = cv2.boundingRect(cnt) #en küçük düz (eksenlere paralel) dikdörtgeni hesaplar. x1.y1 sol üst köşe w-> width, h-> height. Eğer kuş çok çapraz ise bu büyük kutu çizer bu yuzden minAreaRect(cnt) kullanırız.
        cv2.rectangle(img, (x1,y1), (x1+w, y1+h), (0,255,0), 2)
cv2.imshow("img", img)
cv2.imshow("thresh", thresh)

cv2.waitKey(0)