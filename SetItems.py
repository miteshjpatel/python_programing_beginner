thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


print("banana" in thisset)

#  Once a set is created, you cannot change its items, but you can add new items.

thisset.add('orange')

print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

thisset.remove('banana')

print(thisset)
# union example
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#update example
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#update and union will remove duplicate
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3, "a"}

set1.update(set2)
print(set1)

# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

x.add








