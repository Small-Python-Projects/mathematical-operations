import math

def area(radius):
    
    area = float((math.pi)*radius*radius)
    
    area = str(format(area, '.3f'))

    return area;
    
def circumference(radius):
    
    circumference = float((math.pi)*radius*2)
    
    circumference = str(format(circumference, '.3f'))

    return circumference;
  