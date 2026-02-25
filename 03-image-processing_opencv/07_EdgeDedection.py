import cv2
import numpy as np

img = cv2.imread("Photos/Photo1.jpg") #imleci de gözden kaçırmayalım :)

img_edge = cv2.Canny(img, 100, 200) #standart, kenarları buluyor  

img_edge_d = cv2.dilate(img_edge, np.ones((2,2), dtype=np.int8)) #çizgileri kalınlaştırdık 2x2 bir ekleme yaptı

cv2.imshow('img', img)
cv2.imshow('img_edge',img_edge)
cv2.imshow('img_edge_d',img_edge_d)

cv2.waitKey(0)