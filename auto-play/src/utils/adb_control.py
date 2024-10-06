import os
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