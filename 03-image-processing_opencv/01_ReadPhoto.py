import cv2  # opencv-python kütüphanesini indirerek cv2 paketini kullanabilirsin

photo = cv2.imread("Photos/Sample.jpg")

#cv2.imwrite("Photos/Sampleout.jpg",photo) Yazdırdım tekrar resmi

print(photo.shape) #Output : (344, 612, 3), burada ki 3 aslında 3 boyut(channels) gibi düşünülebilir, 3 boyutlu 344*612 pikseli olan bir resim
cv2.imshow('img',photo)
cv2.waitKey(0)

