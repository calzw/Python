#TEMPERATURE CONVERSION
import sys

unit = input("Choose your unit of measurement (C or F): ")
num = float(input("Input the temperature: "))

if unit == "C":
    num = num * (9 / 5) + 32
    unit = "Fahrenheit"

elif unit == "F":
    num = (num - 32) * (5 / 9)
    unit = "Celsius"

else:
    print(f"{unit} is invalid")
    sys.exit(1)

print(f"{round(num, 2)} degrees {unit}")