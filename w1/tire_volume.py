import math

width = int(input('Enter the width of the tire in mm (ex 100): '))
aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 80): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 5): '))
approximate_volume = round((math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000), 2)
print(f'The approximate volume of the tire with the given dimensions is: {approximate_volume} cubic mm')