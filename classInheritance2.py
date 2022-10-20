# Class Inheritance

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname  = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, cname, gyear):
        super().__init__(fname, lname)
        self.collage = cname
        self.graduateyear = gyear
    
    def printname(self):
        print(self.firstname, self.lastname, self.collage)
        print("Welcom", self.firstname, self.lastname, "to the class of", self.graduateyear, "from", self.collage)


x = Student("Mitesh", "Patel", "Clemson", 1995)
x.printname()