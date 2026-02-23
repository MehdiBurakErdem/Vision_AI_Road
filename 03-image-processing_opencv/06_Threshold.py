import cv2

img = cv2.imread("Photos/Photo1.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ## Genelde threshold işlemi gri görüntü üzerinde yapılır çünkü tek kanallıdır.

ret, sp_thresh = cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY) #ret(eşik değer) 80 -> 80 den büyükler 255(beyaz) olur küçükler ise 0(siyah) atanır.
# 255 burada 8-bit görüntüde maksimum parlaklık değeridir.

#thresh = cv2.blur(sp_thresh, (10,10))
#ret, thresh = cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY) #ret(eşik değer) 80 -> 80 den büyükler 255(beyaz) olur küçükler ise 0(siyah) atanır.
#Bazı görseller için daha iyi bir sonuç alabiliriz blur + thresh yöntemi ile

cv2.imshow("img", img)
cv2.imshow("simple thresh", sp_thresh)

cv2.waitKey(0)
