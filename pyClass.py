# Python Class

class MyClass:
    x = 5
    y = 10


p1 = MyClass()
print(p1.y)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def __str__(self):
        return f"{self.name}({self.age})"
        
        # Object Method myfucn print statement and name
    def myfunc(self):
        print("Hello my name is " + self.name + "I am " + str(self.age) + " year old") 


p2 = Person("John", 36)        

print(p2.age, p2.name)
print(p2)
p2.myfunc()
p2.age = 50
p2.myfunc()