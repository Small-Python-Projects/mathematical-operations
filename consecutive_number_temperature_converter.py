c1 = int(input("Enter the first temperature in celcius: "))
    
c2 = int(input("Enter the second temperature in celcius: "))

for num in range(c1,c2):
    
    Fcon = float((9/5)*num)+32
    
    Fcon = str(format(Fcon, '.1f'))
    
    num = str(num)
    
    print(num+"C in fahrenheit is "+Fcon+"F")

