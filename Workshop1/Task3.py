"""
Write a program that converts the temperature in Fahrenheit
to the temperature in Celsius. Your program should prompt the
user for the temperature and then print “The temperature is XXX
degrees Celsius”.

For example:
Give the temperature in Fahrenheit? 100
The temperature is 37.7777777778 degrees Celsius.
NOTE: The conversion from F degrees Fahrenheit to C degrees
Celsius is: C = (F − 32) × 5/9.
"""

F = float(input("Give the temperature in Fahrenheit? "))
C = (F - 32) * 5/9
print("The temperature is", C, "degrees Celsius.")
