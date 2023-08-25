import math

def print_area(radius):
    
    r = float(input("Enter the radius of your circle: "))
    
    area = float((math.pi)*r*r)
    
    area = str(format(area, '.3f'))

    print("The area of your circle is: "+area)

    return;
    
def area(radius):
    
    radius = float(input("Enter the radius of your circle: "))
    
    area = float((math.pi)*radius*radius)
    
    area = str(format(area, '.3f'))

    print("The area of your circle is: "+area)

    return area;
    
def circumference(radius):
    
    radius = float(input("Enter the radius of your circle: "))
    
    if (radius <= 0):
        
        print("The radius value entered is not valid, please re-run and try again")
    
    elif(radius > 0):
        
        circumference = float((math.pi)*radius*2)
    
        circumference = str(format(circumference, '.3f'))

        print("The circumference of your circle is: "+circumference)

    return radius;
    
x = str.lower(input("If you'd like to work out the area of your circle, type 'a'. If you'd like to work out the circumference, type 'c': "))    

if (x == "a"):

    print_area("")

elif (x == "c"):
    
    circumference("")
