class Rectangle:
    def __init__(self):
        self.height=0
        self.bidth=0

    def setDimention(self,a,b):
        self.height=a
        self.bidth=b

    def showDimention(self):
        print("Height= ",self.height)
        print("Bidth= ",self.bidth)

    def getArea(self):
        return self.height*self.bidth
    
r1= Rectangle()
r1.setDimention(10,12)
print(r1.getArea())