from utils.capture_window import WindowCapture
from utils.image_processor import ImageProcessor
from time import sleep
import cv2 as cv
from utils.game_center import GameCenter


window_name = "LDPlayer"
model_path = "D:\\Workspace\\TreasureHunter\\auto-play\\src\\best.pt"

velocity = 100
sleep_time = 2

window_capture = WindowCapture(window_name)
image_processor = ImageProcessor(model_path, velocity)
game_center = GameCenter(window_capture.hwnd)



while(True):
    ss = window_capture.get_screenshot()
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    actions = image_processor.process_image(ss)
    game_center.move(actions)
    sleep(sleep_time)
    
print('Finished.')