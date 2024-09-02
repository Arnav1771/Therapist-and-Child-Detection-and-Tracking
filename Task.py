from ultralytics import YOLO

model= YOLO('yolov8m.pt')

results = model.track(source = 'Test2.mp4',show = True,tracker="bytetrack.yaml")