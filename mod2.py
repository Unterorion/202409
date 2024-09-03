pi = 3.14159265358979323846

class circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi*(self.radius**2)
    
def add(a,b):
    return a + b