# List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

newlist.clear()  # Clear newlist

print(newlist)

newlist = [x for x in fruits if "a" in x]  #Short form single line code above for loop

print(newlist)
