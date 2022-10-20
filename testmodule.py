# Python test mymodule
import mymodule
import mymodule as mitesh
import platform     #Import build in modules

mymodule.greeting("Mitesh Patel")
mitesh.greeting("Mitesh")
mitesh.person1["name"] = "New Name"

a = mymodule.person1["age"]
b = mitesh.person1["name"]
print(a)
print(b)

x = dir(platform)
print(x)