import cv2

#image = cv2.imread("C:\\Users\\mehdi\\OneDrive\\Pictures\\images\\Sample.jpg")

#print(image.shape)

#cv2.imshow("İmage",image)
#cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0) #kamerayı al

while True:
    ret, frame = cap.read() #if ret == False  Kameradan görüntü alınamamış 
    
    if not ret:
        print("Kameradan görüntü alinamadi.")
        break
    
    cv2.imshow("Camera", frame)
    
    if cv2.waitKey(1) == ord("q"):
        break
    
cap.release() #kamerayı serbest bırak
cv2.destroyAllWindows()