from ultralytics import YOLO

# Hazır YOLO11 Nano modelini yükle
model = YOLO("yolo11n.pt")

# Modeli eğit
results = model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=4
)