# Author: Jordan Erick Larcher
# Course: CSE 111

import math

# variables declaration and input from user
name = input("What's your name ? ").capitalize()

w = float(input(f"{name} enter the width of tire in millimeters: "))
a = float(input(f"{name} enter the aspect ratio of the tire: "))
d = float(input(f"{name} enter the diameter of the wheel in inches: "))

# result computation where v is the volume in liters

v = (math.pi * (pow(w, 2) * a * (w * a + 2540 * d))) / 10000000000
v = round(v, 2)
# Displaying the results

print(f" {name.capitalize()} the inputs you entered are: w: {w}, a: {a} and d: {d}")
print(f"This is the result for a volume of a tire: {v}")
