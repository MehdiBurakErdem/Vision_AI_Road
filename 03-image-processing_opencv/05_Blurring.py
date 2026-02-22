import cv2

img = cv2.imread("Photos/Photo1.jpg")

k_size = 9

img_sblur = cv2.blur(img, (k_size,k_size)) # 9x9 alanda ki piksellerin ortalmasını alır ve 0,0 pikseline koyar sonra bir birim yana gider ve orada alır yine ortalmayı bunu da 0,1 koyar bu şekil devam eder
img_medblur = cv2.medianBlur(img, (k_size)) # 9x9 alandaki ortanca(median) değeri alır, gürültüyü azaltır, kenarları korur
img_gblur = cv2.GaussianBlur(img, (k_size, k_size), 0)  # Gaussian ağırlıklı ortalama alır(ortadakiler daha fazla etkiler) bu da görüntünün kenarlarının daha yumuşak ama doğal kalmasını sağlar

cv2.imshow("Image", img)
cv2.imshow("Standart blur",img_sblur)
cv2.imshow("Median blur",img_medblur)
cv2.imshow("Gaussian blur",img_gblur)


cv2.waitKey(0)