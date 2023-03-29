class Circle:
    def __init__(self,r):
        self.radius= r
    
    def area(self):
        return 3.14*self.radius**2
    
    def circumference(self):
        return 2*3.14*self.radius

c1= Circle(12)
c2= Circle(10)

print(c2.area())
print(c1.area())
print(c1.circumference())
