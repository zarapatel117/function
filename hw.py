import math

def calculate_circumference(radius):
    
    if radius < 0:
        return 
    return 2 * math.pi * radius

radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference (radius)
print("The circumference of the circle is: ",circumference)

print("Please enter a valid number for the radius.")