# Python - Loop Tuples and Join Tuples

thistuple = ("apple", "banana", "cherry")

# Iterate through the items and print the values:

print('Iterate through the items and print the values:')
for x in thistuple:
  print(x)

# Print all items by referring to their index number:
print('Print all items by referring to their index number:')
for i in range(len(thistuple)):
  print(thistuple[i])  


#Print all items, using a while loop to go through all the index numbers:
print("While loop with index:")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1  

# Join Two Tuples
# 

print('Join Two Tuples:')
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


