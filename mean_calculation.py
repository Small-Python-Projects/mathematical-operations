n = 0.0

counter = 1.0

x = float(input("Input numbers to calculate the mean: "))

while (x != ""):

    n = n + x
    
    x = input("Add another if you like: ")
    
    if (x != ""):

        x = float(x)
        
        counter = counter + 1
    
answer = str(n/counter)

print("The answer is: "+answer)
    
