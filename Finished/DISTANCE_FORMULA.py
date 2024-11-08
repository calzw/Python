#DISTANCE FORMULA

import math

print("Hello please input the first set of coordinates below")
print("Point A:")

pointAx = float(input("X: "))
pointAy = float(input("Y: "))

print("Now please input the second set of coordinates below")
print("Point B: ")

pointBx = float(input("X: "))
pointBy = float(input("Y: "))

distance = math.sqrt(pow(pointBx - pointAx, 2) + pow(pointBy - pointAy, 2))

print(f"The distance between the points is {round(distance, 2)}cm")