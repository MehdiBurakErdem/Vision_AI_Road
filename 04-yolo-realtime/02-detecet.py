from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("C:\\Users\\mehdi\\OneDrive\\Desktop\\Vision_AI_Road\\04-yolo-realtime\\image.jpg")

result = results[0]

print("------------------------------------------------------------\n", results , "\n------------------------------------------------------------")

print("\nObjelerin konumu", result.boxes.xyxy)

results[0].show()
