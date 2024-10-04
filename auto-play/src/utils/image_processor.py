import cv2 as cv
from ultralytics import YOLO  

class ImageProcessor:
    def __init__(self, img_size, model_path):
        cv.namedWindow('DETECTED OBJECTS', cv.WINDOW_NORMAL)
        cv.resizeWindow('DETECTED OBJECTS', img_size[0], img_size[1])
        self.model = YOLO(model=model_path) 
        
    def process_image(self, img):
        # Perform inference
        results = self.model(img, conf=0.9)[0]
        
        # Get the center of the image
        center_x, center_y = self.get_center(img)

        # Extract predictions
        coordinates = self.get_coordinates(results, center_x=center_x, center_y=center_y)

        # Draw identified objects
        self.draw_identified_objects(img, coordinates)

        return coordinates

    def get_coordinates(self, results, center_x, center_y):
        desired_classes = [3, 5, 6]
        coordinates = []
        for r in results.boxes:
            x1, y1, x2, y2 = map(int, r.xyxy[0])  # Bounding box coordinates
            class_id = int(r.cls[0])  # Class ID
            confidence = r.conf[0]  # Confidence score
            if class_id not in desired_classes:
                continue
            
            center_class = (x1 + x2) // 2, (y1 + y2) // 2
            coordinates.append({
                'x': x1, 
                'y': y1, 
                'w': x2 - x1, 
                'h': y2 - y1, 
                'class': class_id, 
                'confidence': confidence, 
                'class_name': self.model.names[class_id],
                'name'
                "distance": ((center_x - center_class[0]) ** 2 + (center_y - center_class[1]) ** 2) ** 0.5
            })
        return coordinates

    def draw_identified_objects(self, img, coordinates):
        for coordinate in coordinates:
            x = coordinate['x']
            y = coordinate['y']
            w = coordinate['w']
            h = coordinate['h']
            class_name = coordinate['class_name']
            confidence = coordinate['confidence']
            
            color = (0, 255, 0)  # Color for bounding box
            cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
            text = f"{class_name} {confidence:.2f}"
            cv.putText(img, text, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        # Create rectangle around the center of the image, color: red
        center_x, center_y = self.get_center(img)
        cv.rectangle(img, (center_x - 5, center_y - 5), (center_x + 5, center_y + 5), (0, 0, 255), 2)

        
        cv.imshow('DETECTED OBJECTS', img)
        cv.resizeWindow('DETECTED OBJECTS', img.shape[1], img.shape[0])

    def get_center(self, img):
        height, width, _ = img.shape
        center_x = width // 2
        center_y = height // 2
        return center_x, center_y
