import math
import pyautogui

class Calculator:
    @staticmethod
    def distance_2d(point1, point2):
        (x1, y1) = point1
        (x2, y2) = point2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    @staticmethod
    def find_nearly_distance(coordinates):
        if not coordinates:
            return {}

        return min(coordinates, key=lambda x: x['distance'])
    
    @staticmethod
    def find_action(a, b, velocity):
        (ax, ay) = a
        (bx, by) = b
        c = (bx, ay)
        
        h_walk = Calculator.distance_2d(a, c) / velocity
        v_walk = Calculator.distance_2d(b, c) / velocity
        
        # Return the action to move from point A to point B with output format: [(action, press_time), ...]
        actions = []
        # Horizontal walk
        if ax > bx:
            actions.append(('a', h_walk))
        elif ax < bx:
            actions.append(('d', h_walk))
        # Vertical walk    
        if ay > by:
            actions.append(("s", v_walk))
        elif ay < by:
            actions.append(('w', v_walk))
            
        return actions
        
        
        
        
        