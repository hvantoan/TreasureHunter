import cv2 as cv    
from ultralytics import YOLO  
from utils.calculator import Calculator as cal

class ImageProcessor:
    
    def __init__(self, model_path, velocity = 0.1):
        cv.namedWindow('Treasure Hunter BOT', cv.WINDOW_AUTOSIZE)
        self.model = YOLO(model=model_path)
        self.velocity = velocity
        
    def process_image(self, img):
        # Perform inference
        results = self.model(img, conf=0.9)[0]
        
        # Get the center of the image
        a = self.get_center(img)

        # Extract predictions
        coordinates = self.get_coordinates(results, a[0], a[1])
        
        # Best target
        coordinate = cal.find_nearly_distance(coordinates)        
        b = coordinate['center']    
        
        # Find actions to move from point A to point B
        actions = cal.find_action(a, b, self.velocity)
        
        # Draw identified objects
        self.draw_identified_objects(img, coordinates)
        
        return actions

    def get_coordinates(self, results, c_img_x, c_img_y):
        desired_classes = [3, 5, 6]
        coordinates = []
        for r in results.boxes:
            x1, y1, x2, y2 = map(int, r.xyxy[0])  # Bounding box coordinates
            confidence = r.conf[0] 
            class_id = int(r.cls[0]) 
            if class_id not in desired_classes:
                continue
            
            center_class = ((x1 + x2) // 2, (y1 + y2) // 2)
            coordinates.append({
                'x': x1, 
                'y': y1, 
                'w': x2 - x1, 
                'h': y2 - y1, 
                'class': class_id, 
                'confidence': confidence, 
                'class_name': self.model.names[class_id],
                'center': center_class,
                'distance': cal.distance_2d((c_img_x, c_img_y), center_class)
            })
            
        return coordinates

    def draw_identified_objects(self, img, coordinates, draw_all=False):
        # Create rectangle around the center of the image, color: red
        (center_x, center_y) = self.get_center(img)
        cv.rectangle(img, (center_x - 1, center_y - 1), (center_x + 1, center_y + 1), (0, 0, 255), 2)
        
        # Draw the line between the center of the image and the nearest object
        coordinate = cal.find_nearly_distance(coordinates)        
        point = coordinate['center']    
        cv.line(img, (center_x, center_y), point, (255, 0, 0), 2)
        
        # Draw horizontal line at the center of the image
        self.draw_right_triangle(img, (center_x, center_y), point)
        
        if draw_all:
            # Draw all objects
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
                cv.putText(img, text, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.4, color, 2)
        else:
            # Draw the nearest object
            x = coordinate['x']
            y = coordinate['y']
            w = coordinate['w']
            h = coordinate['h']
            class_name = coordinate['class_name']
            confidence = coordinate['confidence']
            
            color = (0, 255, 0)  # Color for bounding box
            cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
            text = f"{class_name} {confidence:.2f}"
            cv.putText(img, text, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.4, color, 2)
        
        cv.imshow('Treasure Hunter BOT', img)

    def get_center(self, img):
        height, width, _ = img.shape
        center_x = width // 2
        center_y = height // 2
        return (center_x, center_y)
    
    def draw_right_triangle(self, image, a, b): # a: center of the image, b: center of the nearest object
        (cx, cy) = (b[0], a[1])
        cv.line(image, a, (cx, cy), (0, 255, 0), 2)
        cv.line(image, b, (cx, cy), (0, 255, 0), 2)
        
    
    
   
