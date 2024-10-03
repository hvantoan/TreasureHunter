import cv2 as cv
import numpy as np
from ultralytics import YOLO  # New YOLOv8 library

class ImageProcessor:
    def __init__(self, img_size, model_path):
        self.W = img_size[0]
        self.H = img_size[1]
        self.model = YOLO('best.pt')  # Load YOLOv8 model
        
    def proccess_image(self, img):
        # Resize the image to model input size (640x640 for YOLOv8 by default)
        img_resized = cv.resize(img, (640, 640))
        
        # Perform inference
        results = self.model(img_resized)[0]
        
        # Extract predictions
        coordinates = self.get_coordinates(results)
        
        # Draw identified objects
        self.draw_identified_objects(img, coordinates)

        return coordinates

    def get_coordinates(self, results):
        coordinates = []
        for r in results.boxes:
            x1, y1, x2, y2 = map(int, r.xyxy[0])  # Bounding box coordinates
            class_id = int(r.cls[0])  # Class ID
            confidence = r.conf[0]  # Confidence score
            
            coordinates.append({
                'x': x1, 
                'y': y1, 
                'w': x2 - x1, 
                'h': y2 - y1, 
                'class': class_id, 
                'confidence': confidence, 
                'class_name': self.model.names[class_id]
            })
        return coordinates

    def draw_identified_objects(self, img, coordinates):
        for coordinate in coordinates:
            x = coordinate['x']
            y = coordinate['y']
            w = coordinate['w']
            h = coordinate['h']
            classID = coordinate['class']
            class_name = coordinate['class_name']
            confidence = coordinate['confidence']
            
            color = (0, 255, 0)  # Color for bounding box
            cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
            text = f"{class_name} {confidence:.2f}"
            cv.putText(img, text, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        cv.imshow('DETECTED OBJECTS', img)

# Usage example:
# Create the ImageProcessor object and pass the image size and YOLOv8 model path
# processor = ImageProcessor((1280, 720), 'yolov8n.pt')

# img = cv.imread('input_image.jpg')
# coordinates = processor.proccess_image(img)

# cv.waitKey(0)
# cv.destroyAllWindows()
