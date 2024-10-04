from time import sleep
import pyautogui
import win32gui

class GameCenter: 
    hwnd = None
    
    def __init__(self, hwnd):
        self.hwnd = hwnd
        
    def move(self, actions):
        for action in actions:
            key, press_time = action
            self.send_key(key, press_time)
    
    def send_key(self, key, press_time):
        win32gui.SetForegroundWindow(self.hwnd)
        pyautogui.keyDown(key)
        sleep(press_time)
        pyautogui.keyUp(key)
            