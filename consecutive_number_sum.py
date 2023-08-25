i1 = int(input(print("Enter a starting number: ")))

i2 = int(input(print("Enter a end number: ")))

n = 0

for x in range(i1,i2+1):
    
    n = n+x    
    
    final1 = str(i1)
    final2 = str(i2)
    final3 = str(n)
    
print("Added consecutive integers between "+final1+" and "+final2+" equals "+final3)  
