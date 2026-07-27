import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("C:\\Users\\mehdi\\OneDrive\\Desktop\\Vision_AI_Road\\04-yolo-realtime\\image.jpg")

result = results[0]

image = result.orig_img #piksel dizisi 

for i, class_id in enumerate(result.boxes.cls):
    if int(class_id) == 16:
        x1, y1, x2, y2 = result.boxes.xyxy[i].int().tolist()
        dog = image[y1:y2, x1:x2]
        cv2.imshow(f"Dogs {i}", dog)


cv2.waitKey(0)
cv2.destroyAllWindows()