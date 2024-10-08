import os
import cv2 as cv
class AdbHelper:
    def __init__(self, device_id=None):
        self.device_id = device_id
    def tap(self, x, y):
        self.shell('input tap {} {}'.format(x, y))
        
    def swipe(self, f_point, t_point, duration):
        (x1, y1) = f_point
        (x2, y2) = t_point
        self.shell('input swipe {} {} {} {} {}'.format(x1, y1, x2, y2, duration))
        
    def shell(self, cmd):
        if self.device_id:
            os.system('adb -s {} shell {}'.format(self.device_id, cmd))
        else:
            os.system('adb shell {}'.format(cmd))
    def get_screen_size(self):
        size = self.shell('wm size')
        return size
    
    def get_screen_density(self):
        density = self.shell('wm density')
        return density
    
    def get_screen_resolution(self):
        resolution = self.shell('wm display')
        return resolution
    
    def get_screenshot(self):
        # Capture screen and pull the image to local machine then delete the image on the device
        os.system('adb shell screencap -p /sdcard/screen.png')
        os.system('adb pull /sdcard/screen.png')
        os.system('adb shell rm /sdcard/screen.png')
        return cv.imread('screen.png')