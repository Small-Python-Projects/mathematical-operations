o = str.lower(input("What's the temperature you'd like to convert to? Type 'c' for celcius or 'f' for fahrenheit: "))

if (o == "c"):
    
    f = int(input("Enter the temperature in fahrenheit: ")) 

    Ccon = str((5/9)*(f - 32))
    
    f = str(f)
    
    print(f+"F in celcius is "+Ccon+"C")
    
if (o == "f"):
    
    c = int(input("Enter the temperature in celcius: "))
    
    Fcon = str(((9/5)*c)+32)

    c = str(c)
    
    print(c+"C in fahrenheit is "+Fcon+"F")
