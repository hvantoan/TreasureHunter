import math


class AutoLogic: 
    def find_nearly_distance(self, coordinates):
        min_coordinate: dict = {}
        if len(coordinates) > 0:
            min_distance = coordinates[0]['distance']
            min_coordinate = coordinates[0]
            for coordinate in coordinates:
                if coordinate['distance'] < min_distance:
                    min_distance = coordinate['distance']
                    min_coordinate = coordinate
        return min_coordinate
    
    
      