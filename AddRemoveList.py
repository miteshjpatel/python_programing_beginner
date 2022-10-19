# ADD Remove from ITEM list

thislist = ["apple", "banana", "cherry"]
thislist.append("orange") ## append to insert
print(thislist)

thislist.insert(1, 'Mango') ## insert to list
print(thislist)

#Loop through list

for i in range(len(thislist)):
    print(thislist[i])

thislist.remove('banana')   # Remove banana from list
print(thislist)

thislist.pop(1)             # Remove the specified index
print(thislist)

print(len(thislist))