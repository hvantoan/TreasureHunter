from  utils.capture_window import WindowCapture
from utils.image_processor import ImageProcessor
from time import sleep
import cv2 as cv

window_name = "LDPlayer"
model_path = "D:\\Workspace\\TreasureHunter\\auto-play\\src\\best.pt"

wincap = WindowCapture(window_name)
improc = ImageProcessor(wincap.get_window_size(), model_path)

while(True):
    
    ss = wincap.get_screenshot()
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    coordinates = improc.proccess_image(ss)
    
    for coordinate in coordinates:
        print(coordinate)
    print("---------------  NEXT FRAME  ---------------")
    
    # If you have limited computer resources, consider adding a sleep delay between detections.
    sleep(1)

print('Finished.')


# if __name__ == "__main__":

#     model_path = os.path.join(os.path.dirname(__file__), "best.pt")
#     model = YOLO(model_path, task='detect')
#     # Update the window_name variable with the title of your game window
#     window_name = "LDPlayer"
#     interval_seconds = 1 / 2  # 60 FPS
    

#     wincap = WindowCapture(window_name)
#     plt.ion()  # Turn on interactive mode
#     fig, ax = plt.subplots()
#     img_display = ax.imshow(wincap.get_screenshot()[..., [2, 1, 0]])

#     while True:
#         img = wincap.get_screenshot()
#         results = model(img[..., [2, 1, 0]], conf=0.9)
#         print(results)
#         im = np.ascontiguousarray(img[..., [2, 1, 0]])
     
#         img_display.set_data(im)
#         plt.draw()
#         plt.pause(interval_seconds)

#         if keyboard.is_pressed(hotkey='q'):
#             print("Quitting...")
#             break
