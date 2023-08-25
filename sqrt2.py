import math

x = input("Input a value to find the squareroot: ")

if (x < "0"):
        
    print("Negative values aren't allowed! Please input another value!")
        
elif(x >= "0"):
        
    x = float(x)
        
    y = math.sqrt(x)
        
    if(x >= 0):
    
        y = str(format(y, '.4f'))
        
        x = str(x)
    
        print("The square root of "+x+" is: "+y)
