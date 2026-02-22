import cv2

img = cv2.imread("Photos/Photo1.jpg")

reimg = cv2.resize(img,(600,450)) # img.shape = (height, width, channels) şeklindedir., ancak cv2.resize() fonksiyonu boyutu (width, height) olarak ister.

cropped_img = img[100:850,50:1000] #sol ust koseyi 0 alarak ayarla
print(f"Size of original image: {img.shape}\nSize of resized image: {reimg.shape}\n")

cv2.imshow('original_img', img)
cv2.imshow('resized_img',reimg)
cv2.imshow('cropped_img',cropped_img)
cv2.waitKey(0)