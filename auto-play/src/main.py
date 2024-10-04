from  utils.capture_window import WindowCapture
from utils.image_processor import ImageProcessor
from time import sleep
import cv2 as cv


window_name = "LDPlayer"
model_path = "D:\\Workspace\\TreasureHunter\\auto-play\\src\\best.pt"

window_capture = WindowCapture(window_name)
image_processor = ImageProcessor(window_capture.get_window_size(), model_path)

while(True):
    ss = window_capture.get_screenshot()
    height, width, channels = ss.shape
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    cv.imshow('DETECTED OBJECTS', ss)
    coordinates = image_processor.process_image(ss)

    # Get coordinate has the smallest distance to the center of the image
   

    # for coordinate in coordinates:
    #     print(coordinate)
    print("---------------  NEXT FRAME  ---------------")
    sleep(0.1)

print('Finished.')