class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def show(self):
        print(self.name)
        print(self.age)

mohit= Person("Mohit Sarkar",21)
mohit.show()