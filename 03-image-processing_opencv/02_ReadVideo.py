import cv2

def showVideo():
    video = cv2.VideoCapture("Photos/Monkeys.mp4")

    ret = 1

    fps = video.get(cv2.CAP_PROP_FPS)
    print(fps)

    while ret:
        ret, frame = video.read()

        if ret:
            cv2.imshow("frame", frame)
            cv2.waitKey(40) #40ms bir frame/resmi getir, yani 1saniye de 25 resim gelir bu da demek oluyor ki 25fps(25 Frames Per Second)

    video.release()	#Video/kamera kaynağını bırakır
    cv2.destroyAllWindows()	#Açılan pencereleri kapatır


def showPcCamera():
    cam = cv2.VideoCapture(0) #harici kamera falan olursa kamera ıd'sini yazacaksın

    while True:
        ret, frame = cam.read()

        cv2.imshow('frame',frame)
        if cv2.waitKey(40) & 0xFF == ord('q'): #imshow yap q diye kontrol de et
            break
    
    cam.release()
    cv2.destroyAllWindows()

choose = int(input("Enter 1 to play the video\nEnter 2 to open the PC camera\nYour choice: "))

if choose == 1:
    showVideo()
elif choose == 2:
    showPcCamera()

#Bu sistem CLI -> Komut Satırı Arayüzü -> Terminal gibi düşün bu yağtıımız sistem bu ve opencv guı tabanlı çalıştığından video arka tarafta kalıyor çünkü hala terminal o fonksiyondan bir dönüş bekleyecek
#GUI -> Grafiksel Kullanıcı Arayüzü -> Visual Programming reposuna bakabilirsin orada ki hersey :))