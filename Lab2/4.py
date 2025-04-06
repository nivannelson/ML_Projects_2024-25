'''
Write a program to create a class Box with data members length,
breadth, height, area, and volume. Provider constructor that enables
initialization with one parameter (for cube), two parameters (for
square prism) three parameters (rectangular prism). Also, provide
functions to calculate area and volume.
Create a list of N boxes with random measurements and print the
details of the box with maximum volume: area ratio.
'''

import random

class Box:
    def __init__(self, length, breadth=None, height=None):
        # If only one parameter is given, create a cube
        if breadth is None and height is None:
            self.length = self.breadth = self.height = length
        # If two parameters are given, create a square prism
        elif height is None:
            self.length = self.breadth = length
            self.height = breadth
        # If three parameters are given, create a rectangular prism
        else:
            self.length = length
            self.breadth = breadth
            self.height = height
        
        self.area = self.calculate_area()
        self.volume = self.calculate_volume()

    def calculate_area(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.height * self.length)

    def calculate_volume(self):
        return self.length * self.breadth * self.height

    def __str__(self):
        return (f"Box: Length={self.length}, Breadth={self.breadth}, Height={self.height}, "
                f"Area={self.area}, Volume={self.volume}, Ratio={self.volume / self.area:.3f}")

# Generate N random boxes
N = 10
boxes = [Box(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)) for _ in range(N)]

# Find the box with the maximum volume-to-area ratio
max_ratio_box = max(boxes, key=lambda box: box.volume / box.area)

# Print details of the selected box
print("Box with Maximum Volume-to-Area Ratio:")
print(max_ratio_box)
