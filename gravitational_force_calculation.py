# Program which calculates the gravitational force between two point masses

G = 6.67384e-11 # Gravitational constant (m^3 kg^-1 s^-2)

m1 = float(input("Please enter the value of mass m1 (in kg): "))
m2 = float(input("Please enter the value of mass m2 (in kg): "))
dist = float(input("Please enter the value of the distance between the masses (in m): "))

force = G*m1*m2/(dist**2)

print('The gravitational force between the two masses is ' + str(force) + ' (N)')
