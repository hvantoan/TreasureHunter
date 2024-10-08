import math
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
    def find_action(height, a, b, velocity):
        distance = Calculator.distance_2d(a, b)
        
        control_height = height - height*0.25
        n_plus = control_height - a[1]
        print(n_plus)
        
        from_point = (int(a[0]), int(control_height))
        new_b = (b[0], b[1] + n_plus)
        
        to_point = Calculator.find_point_C(from_point, new_b, 50)
        print(from_point, to_point)
        return (from_point, to_point, distance / velocity * 1000)

    @staticmethod
    def find_point_C(A, B, AC_length):
        # Tọa độ A và B
        x_A, y_A = A
        x_B, y_B = B
        

        # Độ dài AB
        AB_length = math.sqrt((x_B - x_A) ** 2 + (y_B - y_A) ** 2)
        print(AB_length)

        # Vector AB (hướng từ A tới B)
        direction_vector = ((x_B - x_A) / AB_length, (y_B - y_A) / AB_length)

        # Tọa độ C có thể ở phía trước hoặc phía sau A trên đường thẳng AB
        C1 = (int(x_A + direction_vector[0] * AC_length), int(y_A + direction_vector[1] * AC_length))
        C2 = (int(x_A - direction_vector[0] * AC_length), int(y_A - direction_vector[1] * AC_length))
        if (x_B > x_A):
            return C1
        return C2
        
        
        
        