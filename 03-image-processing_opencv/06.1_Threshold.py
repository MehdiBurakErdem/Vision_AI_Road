import cv2

img = cv2.imread("Photos/Photo2_madeai.png")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, sp_thresh = cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY) #ret(eşik değer) 80 -> 80 den büyükler 255(beyaz) olur küçükler ise 0(siyah) atanır.
#Eğer ışık düzensiz ise adaptive daha iyi sonuç verir, karşılaştıralım
adp_thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 33, 20)
# Her piksel için 33x33 komşuluk alanı alınır., bu alanın Gaussian ağırlıklı ortalaması hesaplanır. Bu ortalamadan 20 çıkarılarak lokal eşik değeri oluşturulur, piksel bu lokal eşikten büyükse 255, değilse 0 yapılır.

cv2.imshow("original img", img)
cv2.imshow("simple thresh", sp_thresh)
cv2.imshow("adaptive thresh", adp_thresh)

cv2.waitKey(0)