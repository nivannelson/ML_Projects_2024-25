import math

class DShapes:
    def printVolume(self):
        pass
    
    def printArea(self):
        pass

class Cylinder(DShapes):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def printVolume(self):
        volume = math.pi * self.radius ** 2 * self.height
        print(f"Cylinder Volume: {volume:.2f}")
    
    def printArea(self):
        area = 2 * math.pi * self.radius * (self.radius + self.height)
        print(f"Cylinder Surface Area: {area:.2f}")

class Sphere(DShapes):
    def __init__(self, radius):
        self.radius = radius
    
    def printVolume(self):
        volume = (4/3) * math.pi * self.radius ** 3
        print(f"Sphere Volume: {volume:.2f}")
    
    def printArea(self):
        area = 4 * math.pi * self.radius ** 2
        print(f"Sphere Surface Area: {area:.2f}")

# Example usage
cylinder = Cylinder(3, 5)
cylinder.printVolume()
cylinder.printArea()

sphere = Sphere(3)
sphere.printVolume()
sphere.printArea()