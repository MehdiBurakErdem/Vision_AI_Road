from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

results = model("dataset/test/images/005577_jpg.rf.GThRVAlDpEGyzY9q8VQD.jpg", conf=0.25) #Confidence değeri 0.25'in altında olan detection'ları gösterme
#results2 = model("dataset/test/images/suggested-GYjETikViqwklkqvjUMH_jpg.rf.OKLt9lpzLvwnOw7VjMAp.jpg")

results[0].show()
#results2[0].show()