import cv2

img = cv2.imread("Photos/Photo1.jpg")
img2 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) #Computer Vision da çok kullanılanları seçtim, daha da fazla renk uzayı var 
img3 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #3channelden 1channela düşürdük işlem yapmak çok kolaylaştı
img4 = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

cv2.imshow("img", img)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.imshow("img4", img4)

cv2.waitKey(0)