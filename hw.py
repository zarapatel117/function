import math

def calculate_circumference(radius):
    if radius < 0:
        return None  
    return 2 * math.pi * radius

try:
    radius = float(input("Enter the radius of the circle in decimal: "))
    if radius < 0:
        print("The radius cannot be negative. Please enter a valid radius.")
    else:
        circumference = calculate_circumference(radius)
        print("The circumference of the circle is:" ,circumference)
except ValueError:
    print("Invalid number")
