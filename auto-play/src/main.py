from utils.capture_window import WindowCapture
from utils.image_processor import ImageProcessor
from utils.adb_control import AdbHelper
from time import sleep
import cv2 as cv

window_name = "LDPlayer"
model_path = "D:\\Workspace\\TreasureHunter\\auto-play\\src\\best.pt"

velocity = 180
sleep_time = 2.5

window_capture = WindowCapture(window_name)
image_processor = ImageProcessor(model_path, velocity)
adb_control = AdbHelper("emulator-5554")


while(True):
    ss = window_capture.get_screenshot()
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    f_point, t_point, duration = image_processor.process_image(ss)
    adb_control.swipe(f_point, t_point, int(duration))    
    print("Swipe from {} to {} in {} ms".format(f_point, t_point, int(duration)))
    
    sleep(sleep_time)
    
print('Finished.')