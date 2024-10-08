from utils.capture_window import WindowCapture
from utils.image_processor import ImageProcessor
from utils.adb_control import AdbHelper
from time import sleep
import cv2 as cv
from PIL import Image
import os

window_name = "LDPlayer"
model_path = "D:\\Workspace\\TreasureHunter\\auto-play\\src\\best.pt"

velocity = 80
sleep_time = 2.5
scale  = 1.0

window_capture = WindowCapture(window_name, scale)
image_processor = ImageProcessor(model_path, velocity)
adb_control = AdbHelper("emulator-5554")


while(True):
    ss = adb_control.get_screenshot()
    # gray_img = cv.cvtColor(ss, cv.COLOR_BGR2GRAY)
    # im = Image.fromarray(gray_img)
    # if not os.path.exists('images'):
    #     os.makedirs('images')
    # im.save(f"./images/img_{len(os.listdir('images'))}.jpg")
    
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    f_point, t_point, duration = image_processor.process_image(ss)
    adb_control.swipe(f_point, t_point, int(duration))    
    print("Swipe from {} to {} in {} ms".format(f_point, t_point, int(duration)))
    
    ss = adb_control.get_screenshot()
    gray_img = cv.cvtColor(ss, cv.COLOR_BGR2GRAY)
    im = Image.fromarray(gray_img)
    if not os.path.exists('images'):
        os.makedirs('images')
    im.save(f"./images/img_{len(os.listdir('images'))}.jpg")
    
    sleep(sleep_time)
    
print('Finished.')