# Python Copy List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, 
# and changes made in list1 will automatically also be made in list2.



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruitsNew = fruits   # Wrong

fruits.pop(1)       # Making change to fruits will change fruitsNew

print(fruitsNew)

fruitsNew.clear() # Clearing new list will clear originial in our case fruits

print(fruits)
print(fruitsNew)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruitsNew = []


fruitsNew = fruits.copy()  # Correct way to copy

print(fruitsNew)

fruits.pop(1)

print(fruits)

print(fruitsNew)


