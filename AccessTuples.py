# Python Tuple are Ordered, Unchangable and Allow Duplicates


thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Print the second item in the tuple:
print(thistuple[1])

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

thislist = list(thistuple)
thislist[1] = 'kiwi'
thistuple = tuple(thislist)

print(thistuple)

# Python, we are also allowed to extract the values back into variables. This is called "unpacking":

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# If the number of variables is less than the number of values, you can add an * to the variable name 
# and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


# If the asterisk is added to another variable name than the last, Python will assign values to the variable 
# until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

